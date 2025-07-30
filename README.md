# 📚 Marketplace de Libros (Backend)

Un backend construido con **FastAPI** y **PostgreSQL** para la compraventa de libros de segunda mano, inspirado en Wallapop pero especializado en literatura.

## 🚀 Características
- Registro y login de usuarios con contraseñas encriptadas.
- Autenticación mediante JWT.
- Gestión de usuarios y sus perfiles.
- Preparado para CRUD de libros, mensajería y transacciones.

---

## ⚙️ Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/usuario/libros.git
cd libros
````

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos


```sql
CREATE DATABASE libros;
```

Modificar la URL en `database.py` si es necesario:

```python
DATABASE_URL = "postgresql://postgres:password@localhost/libros"
```

---

## ▶️ Ejecución

Inicie el servidor con Uvicorn:

```bash
uvicorn main:app --reload
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

Documentación automática de endpoints:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Redoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠️ Endpoints básicos

### Registro

```http
POST /register
```

**Body JSON:**

```json
{
  "nombre": "Alejandro",
  "email": "test@correo.com",
  "password": "123456",
  "ciudad": "Jerez"
}
```

### Login

```http
POST /login
```

**Body JSON:**

```json
{
  "email": "test@correo.com",
  "password": "123456"
}
```

Respuesta:

```json
{
  "access_token": "xxxxx.yyyyy.zzzzz",
  "token_type": "bearer"
}
```

### Perfil del usuario

```http
GET /me
```

**Header:**

```
Authorization: Bearer <TOKEN>
```

---

## 📌 Pendiente de implementar

* CRUD de libros (publicación, edición, borrado, búsqueda).
* Mensajería entre usuarios.
* Gestión de transacciones y comisiones.
* Sistema de valoración de usuarios y libros.

---

## 🤝 Contribuciones

Pull requests bienvenidos. Para cambios mayores, abra primero un issue y discútalo.

---

## 🏛️ Licencia

Software libre bajo GNU General Public License v3.0 (GNU GPLv3).

---


