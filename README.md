# AgroProject

AgroProject es una aplicación Django para gestionar terrenos, cultivos y sensores.

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/agro_project.git
   cd agro_project
2. **Crea un Entorno Virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
3. **Instala Dependencias**
   ```bash
   pip install -r requirements.txt
4. **Realiza las migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. **Crea un super usuario**
   ```bash
   python manage.py createsuperuser
6. **Inicia el Servidor**
   ```bash
   python manage.py runserver


