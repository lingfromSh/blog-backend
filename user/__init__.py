"""user app"""
from flask import Blueprint
app_name = "user"
user = Blueprint('user', __name__)

# lazy loading
from .views import *
