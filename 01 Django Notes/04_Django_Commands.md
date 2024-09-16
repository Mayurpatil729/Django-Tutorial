### Folder Structure Example:
```
demoproject1/                   # Main project folder
│
├── demoproject/                 # Project settings directory
│   ├── __init__.py
│   ├── settings.py              # Contains BASE_DIR and TEMPLATE settings
│   ├── urls.py                  # Project-level URL routing
│   └── wsgi.py
│
├── manage.py                    # Django's project management script
│
├── testapp1/                    # First application folder
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/              # Stores migration files
│   ├── models.py
│   ├── tests.py
│   ├── views.py                 # Define view functions
│   └── urls.py                  # Application-specific URLs
│
├── testapp2/                    # Second application folder
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
│
├── templates/                   # Templates folder at the project level
│   ├── testapp1/                # Folder for testapp1's templates
│   │   └── results.html         # Example HTML template for testapp1
│   │
│   ├── testapp2/                # Folder for testapp2's templates
│   │   └── some_template.html   # Example HTML template for testapp2
│   │
└── db.sqlite3                   # Database file (default for Django)

```

### Steps to Set Up Templates:

1. **Start Project**:
   ```bash
   django-admin startproject demoproject1
   ```

2. **Start Applications**:
   ```bash
   python manage.py startapp testapp1
   python manage.py startapp testapp2
   ```

3. **Create `templates` Folder**:
   - Inside your main project folder (`demoproject1`), create a folder named `templates`.
   - Inside `templates`, create subfolders for each app (`testapp1`, `testapp2`).

4. **Update `settings.py`**:
   Add the templates directory path to your `TEMPLATES` setting in the `settings.py` file.
   ```python
   import os
   BASE_DIR = Path(__file__).resolve().parent.parent
   TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [TEMPLATE_DIR],  # Add this line
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
   ]
   ```

5. **Define View Functions in Each App**:
   In `testapp1/views.py`:
   ```python
   from django.shortcuts import render

   def results_view(request):
       return render(request, 'testapp1/results.html')
   ```

   In `testapp2/views.py`:
   ```python
   from django.shortcuts import render

   def some_template_view(request):
       return render(request, 'testapp2/some_template.html')
   ```

6. **Define URL Patterns**:
   In `testapp1/urls.py`:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('results/', views.results_view, name='results'),
   ]
   ```

   In `testapp2/urls.py`:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('some_template/', views.some_template_view, name='some_template'),
   ]
   ```

7. **Run Server**:
   ```bash
   python manage.py runserver
   ```

8. **Send Request**:
   - Visit `http://127.0.0.1:8000/results/` for `testapp1`.
   - Visit `http://127.0.0.1:8000/some_template/` for `testapp2`.

This structure organizes your templates in a centralized `templates/` directory and maintains individual folders for each app's templates.