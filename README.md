# Django REST framework basic template sample application 

This is a basic template application to start the Django REST framework it covers user authentication module(login/logout API) and creation of a new user in the admin panel. It can be used as the base of any new projects and could be used tocode the rest of the API's.

## Running Locally

```bash
https://github.com/bibinjose2/django-rest-framework.git
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py runserver
```

Django admin url: 127.0.0.1:8000/admin/

Login api url: 127.0.0.1:8000/api/login

