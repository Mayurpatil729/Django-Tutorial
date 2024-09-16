<!-- @format -->

Here is the updated and detailed guide for setting up **Tailwind CSS** with Django on Windows OS, including the installation of **Node.js** and **npm**, and addressing common issues.

---

# Tailwind CSS Setup in Django on Windows OS

## Prerequisites

Before integrating Tailwind CSS into your Django project, ensure the following are installed:

- **Python** (3.x)
- **Django**
- **Node.js** and **npm**

### 1. Install Node.js and npm

Tailwind CSS relies on Node.js and npm. Download and install Node.js from the official website:

- **Download Node.js**: [https://nodejs.org/en/download/](https://nodejs.org/en/download/)

Make sure to download the Windows installer (.msi) for your system (either 32-bit or 64-bit).

#### Verify Installation

After installation, verify that Node.js and npm are installed correctly by running:

```bash
node -v
npm -v
```

Both commands should output the version numbers of Node.js and npm, respectively.

## Setting Up Tailwind CSS in Django

### 2. Install `django-tailwind`

Activate your virtual environment and install `django-tailwind` with browser reload support:

```bash
pip install django-tailwind[reload]
```

### 3. Initialize Tailwind in Your Django Project

Navigate to your Django project directory and run:

```bash
python manage.py tailwind init
```

You will be prompted to enter an app name for your Tailwind CSS app. For this guide, we'll use `theme`.

### 4. Update `settings.py`

Add the following configurations to your `settings.py`:

#### a. Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # other installed apps
    'tailwind',
    'theme',  # Replace 'theme' with your actual Tailwind app name if different
    'django_browser_reload',
]
```

#### b. Set the `TAILWIND_APP_NAME`:

```python
TAILWIND_APP_NAME = 'theme'  # Replace 'theme' with your Tailwind app name
```

#### c. Add `django_browser_reload` middleware:

```python
MIDDLEWARE = [
    # other middleware classes
    'django.middleware.security.SecurityMiddleware',
    # ...
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]
```

### 5. Install Tailwind Dependencies

Install Tailwind CSS and its dependencies:

```bash
python manage.py tailwind install
```

#### **Troubleshooting: CommandError**

If you encounter the following error:

```
CommandError:
It looks like node.js and/or npm is not installed or cannot be found.

Visit https://nodejs.org to download and install node.js for your system.

If you have npm installed and still getting this error message, set NPM_BIN_PATH variable in settings.py to match path of NPM executable in your system.

Example:
NPM_BIN_PATH = "/usr/local/bin/npm"
```

##### **Solution:**

1. **Verify Node.js and npm Installation**

   Ensure Node.js and npm are installed and accessible from the command line:

   ```bash
   node -v
   npm -v
   ```

   If these commands don't output the version numbers, Node.js and npm are not installed correctly, or the PATH environment variable is not set properly.

2. **Check System PATH Environment Variable**

   - Open **System Properties**:
     - Press `Win + R`, type `sysdm.cpl`, and press Enter.
   - Go to the **Advanced** tab and click on **Environment Variables**.
   - Under **System Variables**, find and select **Path**, then click **Edit**.
   - Ensure that the path to Node.js (e.g., `C:\Program Files\nodejs\`) is included in the Path variable.
   - If not, click **New** and add the path to your Node.js installation directory.

3. **Set `NPM_BIN_PATH` in `settings.py`**

   Add the following line to your `settings.py`, pointing to your npm executable:

   ```python
   NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
   ```

   **Note:** Use `npm.cmd` on Windows, not just `npm`.

4. **Restart Your Command Prompt or IDE**

   If you made changes to the system environment variables, restart your command prompt or IDE to apply the changes.

5. **Retry the Tailwind Install Command**

   Run the install command again:

   ```bash
   python manage.py tailwind install
   ```

### 6. Start the Tailwind CSS Compiler

To watch for changes and compile your Tailwind CSS in development mode with hot reloading, run:

```bash
python manage.py tailwind start
```

### 7. Include Tailwind CSS in Your Django Templates

In your base template (`base.html` or similar), include the compiled Tailwind CSS file:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Other meta tags -->
    <link href="{% static 'css/dist/styles.css' %}" rel="stylesheet" />
    <!-- If using django_browser_reload -->
    <script src="http://localhost:8000/static/django_browser_reload/reload.js"></script>
  </head>
  <body>
    <!-- Your content -->
    {% load django_browser_reload %} {% django_browser_reload %}
  </body>
</html>
```

### 8. Collect Static Files (For Production)

When you're ready to deploy, collect static files:

```bash
python manage.py collectstatic
```

## Additional Notes

### Using `static` in Templates

Ensure you have `{% load static %}` at the top of your templates when using the `{% static %}` template tag:

```html
{% load static %}
<link href="{% static 'css/dist/styles.css' %}" rel="stylesheet" />
```

### Creating Tailwind CSS Styles

Edit your Tailwind CSS files in the `theme/static_src/` directory. The main entry point is usually `input.css`.

### Important Paths and Files

- **Tailwind App Directory**: `theme/`
- **Tailwind Static Source**: `theme/static_src/`
- **Compiled CSS Output**: `theme/static/css/dist/styles.css`

## Common Issues and Solutions

### Node.js and npm Not Recognized

**Error**:

```
'node' is not recognized as an internal or external command,
operable program or batch file.
```

**Solution**:

- Ensure Node.js is installed.
- Add the Node.js installation directory to your system PATH.
- Restart your command prompt or IDE.

### `NPM_BIN_PATH` Incorrect

Ensure that `NPM_BIN_PATH` in `settings.py` points to `npm.cmd` on Windows:

```python
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
```

### Permissions Issues

If you run into permissions issues, try running your command prompt or terminal as an administrator.

## Final Steps

After completing the setup:

1. **Run the Django Development Server**:

   ```bash
   python manage.py runserver
   ```

2. **Run Tailwind in Watch Mode**:

   ```bash
   python manage.py tailwind start
   ```

3. **Access Your Application**:

   Visit `http://localhost:8000/` in your browser. Changes to your Tailwind CSS files should reflect automatically.

---

By following these steps, you should have Tailwind CSS properly set up with Django on Windows OS, along with hot reloading capabilities provided by `django-browser-reload`.

If you encounter any further issues, consider checking:

- The official documentation for [django-tailwind](https://django-tailwind.readthedocs.io/en/latest/).
- The GitHub repository for known issues and solutions.
- Ensure all paths in `settings.py` and environment variables are correct.

---
