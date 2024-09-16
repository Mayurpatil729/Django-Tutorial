## 1. Applications

### To Create an Application

```bash
# Navigate to your project directory and run the following command:
python manage.py startapp ApplicationName
```
_Example:_

```bash
PS M:\DjangoProjects01\firstproject> python manage.py startapp myapp
```

---

### 2. Steps to Create the Application

1. **Start Project**: Create your Django project.
   ```bash
   django-admin startproject ProjectName
   ```
2. **Start Application**: Use the command above to create an application.
3. **Add Application to Project**:
   - Open the `settings.py` file inside your project directory.
   - Locate the `INSTALLED_APPS` list and add your application's name.
   ```python
   INSTALLED_APPS = [
       'ApplicationName',
       ...
   ]
   ```
4. **Define View Function**: Create a function inside `views.py` of your application.
   ```python
   # views.py
   from django.http import HttpResponse

   def hello(request):
       return HttpResponse("Hello, World!")
   ```
5. **Define URL Pattern**:
   - Create a `urls.py` file in your application directory (if not already there).
   - Define the URL pattern for your view function.
   ```python
   # urls.py (inside application directory)
   from django.urls import path
   from . import views

   urlpatterns = [
       path('hello/', views.hello, name='hello'),
   ]
   ```

6. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

7. **Send Request**: Open a browser and navigate to:
   ```
   http://127.0.0.1:8000/hello
   ```

---

## 3. Additional Notes

- Install Django extension for code suggestions and autocompletion in your code editor.
- Include Emmet language support for faster HTML coding.

---

### URL Example:

```
http://127.0.0.1:8000/hello
```

---

## 4. Notes on Code Structure

1. **Python-related Business Logic**:  
   - Handled inside `views.py`.
  
2. **HTML-related Presentation Logic**:  
   - Defined in the template files (inside the `templates` folder).

