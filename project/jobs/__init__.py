"""
The jobs blueprint handles the user management for this application.
Specifically, this blueprint allows for users to add, and delete
job data from their profile.
"""
from flask import Blueprint

jobs_blueprint = Blueprint('jobs',__name__, template_folder='templates')

from . import routes