"""
ENTERPRISE DIVISION
Updated 11/19/2014 by Steve Katz
"""

from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'wlFw0WP7SrNmAMF1wJaUSjWMTYdTay8EDIA3FPQhbo9c7wQ9rIdQrzJRzcN1o3mp'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        # Updated 11/19/2014 by Steve Katz - Couldn't figure out why this was returning the wrong result, so asked online
        result = a*1.0/b
        return render_template('index.html',session=session,result=result)
    if 'loggedin' in session and session['loggedin']:
        flag = 'woah_that_was_some_nice_session_magic'
        return render_template('index.html',session=session,flag=flag)
    return render_template('index.html',session=session)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'lolthisisaredherringugotrekt!@*#(^':
            session['loggedin'] = True
            return render_template('login.html',session=session,loggedin=True)
        return render_template('login.html',session=session,loggedin=False)
    return render_template('login.html',session=session)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
