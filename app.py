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

@app.route('/forms', methods=["GET"])
def forms():
    return render_template("forms.html"), 200

@app.route('/sql', methods=["GET", 'POST'])
def sql():
    return render_template('sql.html'), 200

@app.route('/html', methods=["GET", 'POST'])
def html():
    return render_template('html.html'), 200

@app.route('/php', methods=["GET", 'POST'])
def php():
    return render_template('php.html'), 200

@app.route('/ldap', methods=["GET", 'POST'])
def ldap():
    return render_template('ldap.html'), 200

@app.route('/rfi', methods=["GET", 'POST'])
def rfi():
    return render_template('rfi.html'), 200

@app.route('/xpath', methods=["GET", 'POST'])
def xpath():
    return render_template('xpath.html'), 200

@app.route('/xss', methods=["GET", 'POST'])
def xss():
    return render_template('xss.html'), 200