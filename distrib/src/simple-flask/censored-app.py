from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

@app.route('/',methods=['GET','POST'])
def index():
    if 'expected_username' not in session:
        session['expected_username'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        session['expected_password'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']

    if 'username' in session:
        if session['username'] == session['expected_username'] and session['password'] == session['expected_password']:
            flag = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            return render_template('index.html',session=session,flag=flag)

    return render_template('index.html',session=session)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
