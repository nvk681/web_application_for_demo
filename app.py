from flask import Flask, render_template, redirect, url_for, request, make_response
app = Flask(__name__)
import re

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
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    if first_name and last_name:
        return '<p>Values saved first name: ' +first_name+' last name: '+ last_name +'</p>'
    return render_template('html.html'), 200

@app.route('/php', methods=["GET", 'POST'])
def php():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    if '1;phpinfo()' in [first_name, last_name]:
        return '<title>phpinfo[()]</title><h1 class="p">PHP Version (1.12)</h1>', 200
    if first_name and last_name:
        return '<p>Values saved first name: ' +first_name+' last name: '+ last_name +'</p>', 200
    return render_template('php.html'), 200

@app.route('/ldap', methods=["GET", 'POST'])
def ldap():
    first_name = request.args.get('first_name')
    last_name = request.args.get('')
    if "(*)*)" in [first_name, last_name]:
        return 'Request failed due to IPWorksASP.LDAP ', 200
    if first_name and last_name:
        return '<p>Values saved first name: ' +first_name+' last name: '+ last_name +'</p>', 200
    return render_template('ldap.html'), 200

@app.route('/rfi', methods=["GET", 'POST'])
def rfi():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    if re.search('boot.ini', first_name) or re.search('boot.ini', first_name):
        return 'Request failed due to root:/root:/bin/bash|default=multi([0])disk([0])rdisk([0])partition([1])\\WINDOWS ', 200
    if first_name and last_name:
        return '<p>Values saved first name: ' +first_name+' last name: '+ last_name +'</p>', 200
    return render_template('rfi.html'), 200

@app.route('/xpath', methods=["GET", 'POST'])
def xpath():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    if re.search('@*', first_name) or re.search('@*', first_name):
        return 'Request failed due to XPathException ', 200
    if first_name and last_name:
        return '<p>Values saved first name: ' +first_name+' last name: '+ last_name +'</p>', 200
    return render_template('xpath.html'), 200

@app.route('/xss', methods=["GET", 'POST'])
def xss():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    if re.search('javascript:alert(xss)', first_name) or re.search('javascript:alert(xss)', first_name):
        return 'Request failed due to javascript:alert(xss) ', 200
    if first_name and last_name:
        return '<p>Values saved first name: ' +first_name+' last name: '+ last_name +'</p>', 200
    return render_template('xss.html'), 200

@app.route('/headers', methods=["GET"])
def headers():
    resp = make_response(render_template("headers.html"))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers["Host-Header"] = '*'
    resp.headers["Liferay-Portal"] = '*'
    resp.headers["Powered-By"] = '*'
    resp.headers["Product"] = '*'
    resp.headers["Server"] = '*'
    resp.headers["SourceMap"] = '*'
    resp.headers["X-AspNet-Version"] = '*'
    resp.headers["X-AspNetMvc-Version"] = '*'
    resp.headers["X-CF-Powered-By"] = '*'
    resp.headers["X-CMS"] = '*'
    resp.headers["X-Content-Encoded-By"] = '*'
    resp.headers["X-Envoy-Upstream-Service-Time"] = '*'
    resp.headers["Cache-Control"] = "no-store, max-age=0"
    resp.headers["Content-Security-Policy"] = "default-src 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests; block-all-mixed-content"
    resp.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    resp.headers["Cross-Origin-Opener-Policy"] = "*"
    resp.headers["Cross-Origin-Resource-Policy"] = "*"
    resp.headers["Permissions-Policy"] = "accelerometer=(),ambient-light-sensor=(),autoplay=(),battery=(),camera=(),display-capture=(),document-domain=(),encrypted-media=(),fullscreen=(),gamepad=(),geolocation=(),gyroscope=(),layout-animations=(self),legacy-image-formats=(self),magnetometer=(),microphone=(),midi=(),oversized-images=(self),payment=(),picture-in-picture=(),publickey-credentials-get=(),speaker-selection=(),sync-xhr=(self),unoptimized-images=(self),unsized-media=(self),usb=(),screen-wake-lock=(),web-share=(),xr-spatial-tracking=()"
    resp.headers["Pragma"] = "no-cache"
    
    return resp