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
