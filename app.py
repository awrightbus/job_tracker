from flask import Flask, escape,render_template , request, session, flash
import logging

app = Flask(__name__)
app.secret_key = '\xc5p]\xdb\xeb*#\xfa\xc7\xf4xW\xea\x7fqdC\xa9\xa7z\x07\x19}\xd8x\xb6\xa0b\xac\xdaE\xd1'




cards = []

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/signin', methods=['GET','POST'])
def signIn():
    if request.method == 'POST':
        name = request.form.get('usern')
        
        return render_template('applied.html', name=name)

    return render_template('signIn.html')

@app.route('/addjob', methods=['GET','POST'])
def add_job():
    if request.method == 'GET':
        app.logger.info('calling the add_job fun')
        return render_template('addJob.html')
    if request.method == 'POST':
        
        session['cname'] = request.form['cname']
        session['position'] = request.form['position']
        session['followUp'] = request.form['followUp']
        session['appliedDate'] = request.form['appliedDate']

        cards.append(session['cname'])
        cards.append(session['position'])
        cards.append(session['followUp'])
        cards.append(session['appliedDate'])
        app.logger.info(cards)
        return render_template('applied.html', cards=cards)



@app.route('/applied')
def applied_for():
    return render_template('applied.html')

