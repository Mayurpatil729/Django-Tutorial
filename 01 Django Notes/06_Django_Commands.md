## Django Setup & Jinja Templates in Windows OS

### 1. Django Installation on Windows OS

To get started with Django, you'll need to have Python installed. Make sure Python is installed by checking the version:

```bash
python --version
```

If Python is installed, you can install Django using pip:

```bash
pip install django
```

### 2. Creating a Django Project

Once Django is installed, you can create a new project using the following command:

```bash
django-admin startproject myproject
```

Navigate into your project directory:

```bash
cd myproject
```

### 3. Starting the Development Server

To run your Django project locally:

```bash
python manage.py runserver
```

### 4. Jinja Template Setup

Django by default uses its own templating engine, but you can configure Jinja as a template engine as well.

#### Step 1: Install Jinja2

```bash
pip install Jinja2
```

#### Step 2: Configure Jinja in Django

Open `settings.py` and update the `TEMPLATES` section as follows to include Jinja2:

```python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'jinja2')],
        'APP_DIRS': False,  # Jinja doesn't support this like Django templates do
        'OPTIONS': {
            'environment': 'myproject.jinja2_environment.environment',
        },
    },
]
```

#### Step 3: Configure Jinja Environment

In your project folder, create a file named `jinja2_environment.py`:

```python
# jinja2_environment.py

from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env
```

Now, Jinja templates are configured and ready to use.

---

## Using Jinja Templates

### 1. How to Use `{% load static %}` in Jinja

Django templates require `{% load static %}` for serving static files (CSS, JS, images), but in Jinja, the `static` function is available globally after configuring the Jinja environment.

Example of loading a static file (CSS or JS) in Jinja:

```html
<link rel="stylesheet" href="{{ static('css/style.css') }}">
```

### 2. Using `{% block content %}{% endblock %}` in Jinja

Django’s `{% block content %}{% endblock %}` allows for template inheritance. This can also be achieved in Jinja with similar syntax.

#### Defining Blocks in the Base Template (base.html):

```jinja
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Site{% endblock %}</title>
    <link rel="stylesheet" href="{{ static('css/style.css') }}">
</head>
<body>
    <header>
        <!-- Header Content -->
    </header>

    <main>
        {% block content %}
        <!-- Child template content will go here -->
        {% endblock %}
    </main>

    <footer>
        <!-- Footer Content -->
    </footer>
</body>
</html>
```

#### Extending the Base Template in a Child Template:

```jinja
{% extends "base.html" %}

{% block title %}
    Home - My Site
{% endblock %}

{% block content %}
    <h1>Welcome to My Site!</h1>
    <p>This is the home page.</p>
{% endblock %}
```

---

### Essential Commands for Django on Windows OS

- **Create a new app**:
  ```bash
  python manage.py startapp myapp
  ```

- **Migrate database changes**:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Create a superuser for admin access**:
  ```bash
  python manage.py createsuperuser
  ```

- **Running tests**:
  ```bash
  python manage.py test
  ```

These are the basic setup steps and usage of Jinja templates in Django for Windows OS.

--- 

