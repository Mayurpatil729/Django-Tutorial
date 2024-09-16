<!-- @format -->

Here’s a structured guide on how to join static files, make changes to `INSTALLED_APPS`, and manage URL configurations, along with proper Emmet settings in VSCode.

---

### Adding Static Files in Django

1. **Join Static Files**:  
   Static files (like CSS, JS, images) should be placed in a `static` directory, and you need to configure Django to serve them.

   - **Create a Static Directory**:
     Create a `static/` folder inside your main project folder (same level as `templates/`).
   
   - **Update `settings.py`**:
     Add the `STATICFILES_DIRS` entry to specify where Django should look for static files.

     ```python
     import os

     STATIC_URL = '/static/'  # Define the base URL for serving static files

     STATICFILES_DIRS = [
         os.path.join(BASE_DIR, 'static'),  # Pointing to the 'static/' directory
     ]
     ```

2. **Using Static Files in Templates**:
   In your HTML files, load the static files using Django’s `{% static %}` template tag.

   Example:
   ```html
   {% load static %}

   <link rel="stylesheet" href="{% static 'css/style.css' %}">
   <img src="{% static 'images/logo.png' %}" alt="Logo">
   ```

---

### Changes to `INSTALLED_APPS`

If you add custom applications, you need to register them in the `INSTALLED_APPS` section of your `settings.py` file.

Example:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testapp1',   # Add your application here
    'testapp2',   # Add your second application here
]
```

---

### Creating `urls.py` in an App

For each app, you need to create an `urls.py` file to handle app-specific routing. You can copy the content from the project's root `urls.py` to make the necessary adjustments.

1. **Root-level `urls.py`**:
   Your project’s main `urls.py` should include references to each app’s `urls.py`.

   Example (`demoproject/urls.py`):
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('testapp1/', include('testapp1.urls')),  # Linking to testapp1
       path('testapp2/', include('testapp2.urls')),  # Linking to testapp2
   ]
   ```

2. **App-level `urls.py`**:
   In your app directories (`testapp1`, `testapp2`), create an `urls.py` file to manage the app-specific URLs.

   Example (`testapp1/urls.py`):
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('results/', views.results_view, name='results'),
   ]
   ```

---

### Emmet Settings for VSCode

Emmet is a powerful tool that speeds up HTML and CSS coding in Visual Studio Code (VSCode). Here’s how to configure it for Django templates and other languages:

1. **Configure Emmet for Django (HTML)**:
   - **Open Settings (JSON)** in VSCode:  
     Press `Ctrl + Shift + P` and type “Preferences: Open Settings (JSON)”.
   
   - **Add the Following Configuration**:
     ```json
     "emmet.includeLanguages": {
         "django-html": "html",
         "javascript": "javascriptreact",
         "css": "css",
         "jinja-html": "html"
     },
     ```

2. **Include Emmet for Other Languages**:
   To enable Emmet for other file types like JavaScript, CSS, etc., include them as follows:

   ```json
   "emmet.includeLanguages": {
       "javascript": "javascriptreact",
       "css": "css",
       "scss": "scss"
   },
   ```

   This ensures Emmet expands properly inside `.html`, `.css`, and `.js` files.

---

By following these steps, you’ll have static files served correctly, applications integrated properly in `INSTALLED_APPS`, URLs set up in each app, and Emmet configured to streamline your coding in VSCode.

