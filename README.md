# Django Rest Framework (DRF) Application Template

## Deploy On Local Without Docker

0. you should have the following requirements installed on your machine  
- python3.11
- postgresql

1. create a python virtual environment and activate
```bash
python3 -m venv .venv
source ./venv/bin/activate
```
2. create the postgres database
```bash
psql -U postgres
```
```psql
CREATE DATABASE "db.django-drf-template";
``` 
3. create `backend.env` file based on `backend.env.example` in `deploy/environments/` directory.
4. migrate the database
```bash
python manage.py makemigrations
python manage.py migrate
```
5. create a superuser
```bash
python manage.py custom_createsuperuser
```
6. run django server
```bash
python manage.py runserver 8000
```
now the app should be accessible on http://localhost:8000

## Deploy On Local With Docker

0. you should have `Docker` installed on your machine  

1. create self-signed ssl certification
```bash
openssl req -x509 -newkey rsa:4096 -keyout deploy/config/ssl/privkey.pem -out deploy/config/ssl/fullchain.pem -days 365 -nodes
```
2. build and run
```bash
docker-compose up --build -d
```
now the app should be accessible on https://localhost  
Note: ignore the certification error on the browser

## Implementation
### Creating new app
1. create a new folder with your new app's name inside apps directory
```bash
mkdir ./apps/<app-name>
```
2. create django app
```bash
python manage.py startapp <app-name> apps/<app-name>
```
3. config the `apps.py` file by adding `apps.` prefix to the name variable inside the class.
4. add `"apps.<app-name>"` into `INSTALLED_APPS` in `core/settings.py`.
5. restart the django server

### Logging 
create logger as following:
```python
import logging

from django.conf import settings

logger = logging.getLogger(settings.LOGGER_NAME)
```