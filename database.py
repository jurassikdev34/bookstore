
"""
Configuración de la base de datos con SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ⚠️ Extraer a variable de entorno en producción.
DATABASE_URL = "postgresql://postgres:password@localhost/libros"

# Motor de conexión a la base de datos
engine = create_engine(DATABASE_URL)

# Sesión para consultas
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos
Base = declarative_base()

