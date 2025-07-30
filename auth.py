
"""
Módulo de autenticación con JWT.
Se encarga de generar y verificar tokens de acceso.
"""

from datetime import datetime, timedelta
from jose import JWTError, jwt

# ⚠️ En producción, use una variable de entorno para la clave secreta.
SECRET_KEY = "supersecreto"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Genera un token JWT firmado.
    
    :param data: Datos a incluir en el token (ej: {"sub": email}).
    :param expires_delta: Duración personalizada del token.
    :return: Token JWT como string.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> str | None:
    """
    Verifica la validez de un token JWT.
    
    :param token: Token a verificar.
    :return: El valor de 'sub' si es válido, None si falla.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

