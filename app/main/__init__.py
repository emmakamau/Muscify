from flask import Blueprint
main = Blueprint('main',__name__)

#We import views and error files from the main folder
from app.main import views
