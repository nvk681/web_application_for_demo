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
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    if request.args.get('mysql'):
        return '<p>failure in MySqlClient</p>', 200
    if request.args.get('mssql'):
        return '<p>Failed to save the data SqlException</p>', 200
    if request.args.get('java'):
        return '<p>failure in saving data java.sql.SQLException</p>', 200
    if request.args.get('postgresql'):
        return '<p>failure in Npgsql.</p>', 200
    if request.args.get('db2'):
        return '<p>failure in due to  \[IBM]</p>', 200
    if request.args.get('interbase'):
        return '<p>failure in Dynamic SQL Error</p>', 200
    if request.args.get('sybase'):
        return '<p>failure in Sybase message:</p>', 200
    if request.args.get('oracle'):
        return '<p>failure in saving the data due to Oracle error</p>', 200
    if request.args.get('sqlite'):
        return '<p>failure in saving the data due to SQLITE_ERROR</p>', 200
    if first_name and last_name:
        return '<p> Saved the data', 200
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