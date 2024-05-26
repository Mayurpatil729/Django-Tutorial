<!-- @format -->

Microsoft Windows [Version 10.0.22631.3155]
(c) Microsoft Corporation. All rights reserved.

M:\DjangoProjects01>python -m venv my_venv

M:\DjangoProjects01>my_venv\Scripts\activate

(my_venv) M:\DjangoProjects01>pip install django
Collecting django
Using cached Django-5.0.3-py3-none-any.whl (8.2 MB)
Collecting asgiref<4,>=3.7.0
Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1
Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Collecting tzdata
Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
Collecting typing-extensions>=4
Downloading typing_extensions-4.10.0-py3-none-any.whl (33 kB)
Installing collected packages: tzdata, typing-extensions, sqlparse, asgiref, django
Successfully installed asgiref-3.7.2 django-5.0.3 sqlparse-0.4.4 typing-extensions-4.10.0 tzdata-2024.1

(my_venv) M:\DjangoProjects01>django-admin version
5.0.3

(my_venv) M:\DjangoProjects01>django-admin startproject firstproject

(my_venv) M:\DjangoProjects01>cd firstproject

(my_venv) M:\DjangoProjects01\firstproject>python manage.py runserver
(my_venv) M:\DjangoProjects01\firstproject>python manage.py runserver 80001
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.

Run 'python manage.py migrate' to apply them.
Django version 5.0.3, using settings 'firstproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

---

#### To Create a Virtual Environment

```
python -m venv my_venv
```

#### To Activate the Scripts

```
my_venv\Scripts\activate
```

#### Installing The Django

```
(my_venv) M:\DjangoProjects01>pip install django
```

#### To Install of Specific Version

```
pip install django==1.11
```

#### To Check Version

```
(my_venv) M:\DjangoProjects01>django-admin --version
```

#### To Create The Project

```
(my_venv) M:\DjangoProjects01>django-admin startproject ProjectName
```

#### To Run The Project

```
(my_venv) M:\DjangoProjects01\firstproject>python manage.py runserver
```

#### Run The Project

```
http://127.0.0.1:8000/

http://localhost:8000/
```

#### To Change the PortNumber

```
python manage.py runserver 8888
```

#### To Create The Application

PS M:\DjangoProjects01\firstproject>

```
python manage.py startapp ApplicationName
```

---

---

### Files Description.

1. **init**.py:
   It is a blank python script.Because of this special file name, Django treated this folder as
   python package.
   Note: If any folder contains **init**.py file then only that folder is treated as Python
   package.But this rule is applicable until Python 3.3 Version.

2. settings.py:
   In this file we have to specify all our project settings and and configurations like
   installed applications, middileware configurations, database configurations etc

3. urls.py:

- Here we have to store all our url-patterns of our project.
- For every view (web page), we have to define separate url-pattern. End user can use

4. url-patterns to access our webpages.
   wsgi.py:

- wsgi  Web Server Gateway Interface.
- We can use this file while deploying our application in production on online server.

5. manage.py:

- The most commonly used python script is manage.py
- It is a command line utility to interact with Django project in various ways like to run
  development server, run tests, create migrations etc.

---

---

#### Role of Web Server:

- Web Server provides environment to run our web applications.
- Web Server is responsible to receive the request and forward request to the
  corresponding web component based on url-pattern and to provide response to the
  end user.
- Django framework is responsible to provide development server. Even Django
  framework provides one inbuilt database sqlite. Special Thanks to Django.
  Note: Once we started Server a special database related file will be generated in our
  project folder structure.
  **db.sqlite3**

---


