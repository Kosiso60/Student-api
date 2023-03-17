# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
from flask_sqlalchemy import SQLAlchemy

from ..app import app  # import the app instance using a relative import

db = SQLAlchemy(app)
