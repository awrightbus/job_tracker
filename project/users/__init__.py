"""
the users blueprint will handle everything from user sign in and sing up , forgotten password , etc

"""

from flask import Blueprint

users_blueprint = Blueprint('users',__name__,template_folder='templates')


from . import routes