# django_tutorial2021

This project follows the official Django tutorial

## Tutorial 1
Install django and check its installed
```
pip3 install django
python3 -m django --version
```

Create a project. A project can be made up of multiple apps
```
django-admin startproject mysite
```

Run the development server to that you can connect from a browser. Press CTRL+C to stop the development server
```
python3 manage.py runserver
```

Create an app within the project. 
```
python3 manage.py startapp polls
```

## Tutorial 2
Create the initial database structure
```
python3 manage.py migrate
```

Create new migration for Question, Choice models in polls app
```
python3 manage.py makemigrations polls
```

Then run ```migrate``` command again

Access models through the django shell. Press CTRL+D to end the Django shell
```
python3 manage.py shell
```

Create a superuser to access django admin pages. Then run the development server
```
python3 manage.py createsuperuser
```

## Tutorial 3

## Tutorial 4

## Tutorial 5