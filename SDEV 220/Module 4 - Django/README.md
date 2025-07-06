# Django Tutorial Project

## Description
This original tutorial was supposed to be **blogs** at [DjangoGirls](https://tutorial.djangogirls.org/en/django_models/).
However, I've chosen **polls** from [docs.djangoproject.com](https://docs.djangoproject.com/en/5.2/intro/tutorial01/).

## Prerequisites
- Python 3.8+ (tested on 3.13)
- pip (comes with Python)
- Windows 11 (instructions below assume PowerShell or CMD on Win11)

## Usage

### 1. Create & Start a Virtual Environment
```bash
# Create (only once)
py -m venv venv

# Activate (every new session)
# — PowerShell
.\venv\Scripts\Activate.ps1

# — CMD
venv\Scripts\activate.bat
```
### 2. Database Setup
```bash
# Generate migration files
py manage.py makemigrations

# Migrations to create the database schema
py manage.py migrate
```

### 5. Create a Superuser (admin)
```bash
py manage.py createsuperuser
# Follow prompts to set username/email/password
```

### 6. Run Development Server
```
py manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the site, and http://127.0.0.1:8000/admin/ to log into the admin interface.

### Admin interface
* Log in at /admin/ with your superuser account.

* Manage Question and Choice entries via the polls app.

### Code
* polls/models.py shows how question and choice are defined.

* polls/admin.py registers models with the admin site.

* polls/views.py and polls/urls.py contain basic view logic and routing.