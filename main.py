from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from security import hash_password

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener la sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.UsuarioResponse)
def register(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    # Verificar si email ya existe
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

