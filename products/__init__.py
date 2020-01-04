from sqlalchemy_utils import database_exists, create_database

from settings import db, app
from .product import Product

if not database_exists(db.engine.url):
   create_database(db.engine.url)
db.init_app(app)
db.create_all()
