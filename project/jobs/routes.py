
from flask import Flask, escape,render_template , request, session, flash, current_app
from .  import jobs_blueprint
import logging

cards = []

@jobs_blueprint.route('/addjob', methods=['GET','POST'])
def add_job():
    if request.method == 'GET':
        current_app.logger.info('calling the add_job fun')
        return render_template('/addJob.html')
    if request.method == 'POST':
        
        session['cname'] = request.form['cname']
        session['position'] = request.form['position']
        session['followUp'] = request.form['followUp']
        session['appliedDate'] = request.form['appliedDate']

        cards.append(session['cname'])
        cards.append(session['position'])
        cards.append(session['followUp'])
        cards.append(session['appliedDate'])

        #logging configuration
        file_handler = logging.FileHandler('flask-add-job.log')
        current_app.logger.addHandler(file_handler)

        #Log that flask app is starting 
        current_app.logger.info('Starting the flask job app')

        return render_template('applied.html', cards=cards)


@jobs_blueprint.route('/applied')
def applied_for():
    return render_template('/applied.html')