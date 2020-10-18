from flask import Flask, escape,render_template , request, session

app = Flask(__name__)
app.secret_key = '\xc5p]\xdb\xeb*#\xfa\xc7\xf4xW\xea\x7fqdC\xa9\xa7z\x07\x19}\xd8x\xb6\xa0b\xac\xdaE\xd1'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/addjob', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('addJob.html')
    if request.method == 'POST':
        
        session['cname'] = request.form['cname']
        session['position'] = request.form['position']

        return render_template('applied.html')



@app.route('/applied')
def applied_for():
    return render_template('applied.html')

