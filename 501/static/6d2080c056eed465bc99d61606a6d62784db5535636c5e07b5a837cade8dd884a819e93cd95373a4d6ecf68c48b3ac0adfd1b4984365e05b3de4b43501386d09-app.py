from flask import Flask, render_template, session, request
import pyotp
import datetime
app = Flask(__name__)
keys = open('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx','r').read().split('\n')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        if 'level' not in session:
            session['level'] = 0
        totp = pyotp.TOTP(keys[session['level']])
        correct = totp.verify(password) or totp.verify(password, datetime.datetime.now()-datetime.timedelta(seconds=15)) or totp.verify(password, datetime.datetime.now()+datetime.timedelta(seconds=15)) # Allow for +- 15s time skew
        if not correct:
            session.pop('level',None)
            return render_template('index.html', session=session, correct=correct)
        session['level'] = session['level'] + 1
        if session['level'] == 500:
            session['loggedin'] = True
        return render_template('index.html', session=session, correct=correct)

    return render_template('index.html', session=session)

if __name__ == '__main__':
    app.secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    app.run(host='0.0.0.0')
