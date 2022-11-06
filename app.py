from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        form_data = request.form
        if form_data['username'] != 'admin' or form_data['password'] != 'password':
            return render_template('403.html'), 403
        else:
            return render_template("home.html"), 200
    return render_template('login.html', error=error)

