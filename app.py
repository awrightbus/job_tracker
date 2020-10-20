from flask import Flask, escape,render_template , request, session, flash
import logging, os

app = Flask(__name__)


#Configure Flask application
config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')

app.config.from_object(config_type)


@app.route('/')
def home():

    return render_template('index.html')


# import blueprints
from project.jobs import jobs_blueprint
from project.users import users_blueprint

#register the blue priints 
app.register_blueprint(jobs_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')



