
"""
Funciones de seguridad: hashing y verificación de contraseñas.
"""

from passlib.context import CryptContext

# Configuración de Passlib con bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Genera un hash seguro para una contraseña.
    """
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    """
    Verifica si la contraseña proporcionada coincide con el hash.
    """
    return pwd_context.verify(plain, hashed)

