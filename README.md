# Microservicio Venta

## Bienvenidos a la instalación del sistema

### Primeros pasos

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tapiagarrido/microservicio_venta.git
   ```

2. **Ingresar a la carpeta de aplicación:**

   ```bash
   cd microservicio_venta
   ```

3. **Instalar un ambiente virtual con Python:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Instalar dependencias del proyecto:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Generar variables de entorno:**

   ```bash
   mv .env.template .env
   ```

6. **Modificar las variables con datos que se comparten con `microservicio_bodega`:**

   - Nota: Debe ser el mismo que se inyecta en el header desde `microservicio_bodega`.
     ```env
     X_SECRET_ESPERADO
     ```

   - Nota: Es el mismo seed de JWT de `microservicio_bodega`.
     ```env
     JWT_SEED
     ```

   - Variables de base de datos después de crear la base de datos:
     ```env
     DB_ENGINE
     DB_NAME
     DB_USER
     DB_PASSWORD
     DB_HOST
     DB_PORT
     ```

7. **Aplicar migración de tablas:**

   ```bash
   python manage.py migrate
   ```

8. **Correr la aplicación:**

   ```bash
   python manage.py runserver
   ```

9. **Esperar llamada desde `microservicio_bodega` y visualizar data.**