# relaypanel ![Django CI](https://github.com/KNaiskes/relaypanel/workflows/Django%20CI/badge.svg)

An API for adding, removing and updating relay devices

Checkout also [relaypanel-frontend](https://github.com/KNaiskes/relaypanel-frontend)

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

# API Paths

**Base url** [localhost:8000/api/](http://localhost:8000/api/)

## GET

| Path          | Result                                           |
| ------------- | -------------                                    |
| relays/       | List of all relays (user has permissions to use) |
| relays/pk     | Single relay                                     |



## POST

| Path           | Result          | Required Parameters | Optional Parameters |
| -------------  | -------------   | -------------       | -------------       |
| api-token-auth | User's token    | username, password  | N/A                 |
| relays/new/    | Add a new relay | name, device        | status              |


## PUT

| Path          | Result        | Required Parameters | Optional Parameters |
| ------------- | ------------- | -------------       | -------------       |
| relays/pk     | Update        | name, device        | status              |


## DELETE

| Path          | Result        |
| ------------- | ------------- |
| relays/pk     | Delete relay  |
