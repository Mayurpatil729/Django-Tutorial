<!-- @format -->

## Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. It takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.

Django is a full-featured web framework that follows the Model-View-Controller (MVC) architectural pattern. It provides a set of tools and libraries for building web applicationss, including an ORM, a templating engine, and a built-in admin interface.

### Django Project vs Django Application:

- A Django project is a collection of applications and configurations which forms a full web application.
  Eg: Bank Project
- A Dango Application is responsible to perform a particular task in our entire web application.
  Eg: loan app
  registration app
  polling app etc

- Project = Several Applications + Configuration Information

1. The Django applications can be plugged into other projects.ie these are reusable.
   (Pluggable Django Applications)
2. Without existing Django project there is no chance of existing Django Application.
   Before creating any application first we required to create project.

## Environment Setup

To get started with Django, you'll need to install it on your computer. You can do this by running the following command in your terminal, after setting up a virtual environment:

### Virtual Environment :

A virtual environment is created on top of an existing Python installation, known as the virtual environment's “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

### Steps:

1. Make sure Python is already installed in our system
   python --version
2. Install django by using pip
   pip install django
   pip install django == 1.11.9
3. To check django version:
   py -m django --version
4.
5.

###### Create Virtual Environment

python3 -m venv .venv

###### for windows

```
python -m venv .venv
```

###### to activate the virtual environment

```
source .venv/bin/activate
```

### for windows

```
.venv\Scripts\activate
```

---

using `uv` to manage virtual environment and other tools. It's rediculously easy and fast.

#### On Windows.

powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

#### With pip.

```
pip install uv
```

### to create a virtual environment

```
uv venv
```

```
source .venv/bin/activate
```

### On Windows.

```
.venv\Scripts\activate

```

```
uv pip install django
```

```
uv pip install -r requirements.txt
```

---

#### To create project use :

```
django-admin startproject firstProject
cd firstProject
```

#### To Run Project :

```
python manage.py runserver
```

To run on particular port

```
python manage.py runserver 8001
```

---
