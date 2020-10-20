from . import users_blueprint 
from flask import render_template, flash, request




@users_blueprint.route('/signin', methods=['GET','POST'])
def signIn():
    if request.method == 'POST':
        name = request.form.get('usern')
        
        return render_template('applied.html', name=name)

    return render_template('/signIn.html')




