
"""
Esquemas Pydantic: validación y serialización de datos.
"""

from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    ciudad: str | None = None

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    ciudad: str | None

    class Config:
        from_attributes = True  # Permite crear desde objetos ORM

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginData(BaseModel):
    email: EmailStr
    password: str

