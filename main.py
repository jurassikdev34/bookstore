
"""
Aplicación principal FastAPI.
Incluye registro, login y consulta de perfil del usuario.
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from security import hash_password, verify_password
from auth import create_access_token, verify_token

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Marketplace de Libros")

# Dependencia: obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/register", response_model=schemas.UsuarioResponse)
def register(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario en el sistema.
    """
    # Verificar si el email ya existe
    db_user = db.query(models.Usuario).filter(models.Usuario.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    new_user = models.Usuario(
        nombre=user.nombre,
        email=user.email,
        password_hash=hash_password(user.password),
        ciudad=user.ciudad
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login", response_model=schemas.Token)
def login(data: schemas.LoginData, db: Session = Depends(get_db)):
    """
    Inicia sesión y devuelve un token JWT válido.
    """
    user = db.query(models.Usuario).filter(models.Usuario.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me", response_model=schemas.UsuarioResponse)
def read_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Obtiene los datos del usuario autenticado mediante token JWT.
    """
    email = verify_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    user = db.query(models.Usuario).filter(models.Usuario.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user

