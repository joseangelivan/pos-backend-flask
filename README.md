# POS Backend Flask + PostgreSQL + API REST

Este proyecto contiene el backend de un sistema de punto de venta con:
- Registro y login de usuarios
- API protegida con JWT
- Configuración inicial para desplegar en Render

## 🚀 Despliegue en Render

1. Crear un nuevo servicio web en Render (tipo Web Service).
2. Añadir una base de datos PostgreSQL en Render.
3. Agregar variables de entorno:
   - `DATABASE_URL`: conexión PostgreSQL
   - `SECRET_KEY`: clave secreta para JWT
4. Subir el contenido de este proyecto a GitHub y conectar con Render.
5. Render detectará `requirements.txt` y `run.py` automáticamente.

## 🧪 Probar API

### Registro
```bash
curl -X POST https://TU_DOMINIO.onrender.com/api/register \
     -H "Content-Type: application/json" \
     -d '{"username": "usuario", "password": "clave"}'
```

### Login
```bash
curl -X POST https://TU_DOMINIO.onrender.com/api/login \
     -H "Content-Type: application/json" \
     -d '{"username": "usuario", "password": "clave"}'
```

### Obtener configuración
```bash
curl -X GET https://TU_DOMINIO.onrender.com/api/config \
     -H "Authorization: Bearer TU_TOKEN"
```
