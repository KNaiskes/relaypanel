# relaypanel

An API for adding, removing and updating relay devices

## Dependencies

- Python 3
- Django
- Django REST framework

## Quick Start

Clone the repository

```
$ git clone https://github.com/KNaiskes/relaypanel
```

Install dependencies

```
$ cd relaypanel
$ python -m venv venv # create a virtual enviroment
$ source venv/bin/activate # activate virtual enviroment
$ pip install -r requirements.txt
```

Database migrations

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Create a super user (admin)

```
$ python manage.py createsuperuser
```

Run development server

```
$ python manage.py runserver
```

Browse to [localhost:8000/admin/](http://localhost:8000/admin/) in order to add
new relay devices or users.
