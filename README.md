[![Build Status](https://travis-ci.org/mbithenzomo/flask-school-app-and-api.svg?branch=master)](https://travis-ci.org/mbithenzomo/flask-school-app-and-api)
[![Code Health](https://landscape.io/github/mbithenzomo/flask-school-app-and-api/master/landscape.svg?style=flat)](https://landscape.io/github/mbithenzomo/flask-school-app-and-api/master)

# School App and API
This is a Flask app with an API layer. It has the following properties:

1. It has the following relational entities:
    1. Student
    2. Teacher
    3. Course
2. Each student can have only one subject as a major, but can read any subject as well (minors)
3. A subject is taught by one teacher
4. It has endpoints to CREATE, UPDATE, and DELETE each entity in the application
5. Only an authorized user can access the endpoints

## Installation and Set Up
Clone the repo from GitHub:
```
git clone https://github.com/Kosiso60/Student-api.git
```


Navigate to the root folder:
```
cd Student-api
```

Install the required packages:
```
pip install -r requirements.txt
```

Create a `.env` file with the following keys:
```
SECRET_KEY
DATABASE_URI - for SQLAlchemy
TEST_DATABASE_URI - for SQLAlchemy
ENVIRONMENT - this is either production or development
```         


## Launching the Program
Run ```python run.py```. You may use [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) for Google Chrome to run the API.

## API Endpoints

| Resource URL | Methods | Description | Requires Token |
| -------- | ------------- | --------- |--------------- |
| `/api/v1` | GET  | The index | FALSE |
| `/api/v1/auth/register` | POST  | User registration | FALSE |
|  `/api/v1/auth/login` | POST | User login | FALSE |
| `/api/v1/students` | GET, POST | View all students, add a student | TRUE |
| `/api/v1/students/<string:id>` | GET, PUT, DELETE | View, edit, and delete a single student | TRUE |
| `/api/v1/teachers` | GET, POST | View all teachers, add a teacher | TRUE |
| `/api/v1/teachers/<string:id>` | GET, PUT, DELETE | View, edit, and delete a single teacher | TRUE |
| `/api/v1/courses` | GET, POST | View all subjects, add a subject | TRUE |
| `/api/v1/courses/<string:id>` | GET, PUT, DELETE | View, edit, and delete a single subject | TRUE |



Registering and logging in to get a JWT token

## Built With...
* [Flask](http://flask.pocoo.org/)
* [Flask-RESTX](http://flask-restful-cn.readthedocs.io/en/0.3.4/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

## Credits
An AltSchool Africa 3rd semester project
