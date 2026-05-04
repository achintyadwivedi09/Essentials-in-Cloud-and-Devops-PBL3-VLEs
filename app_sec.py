from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates_sec")

USERNAME = "admin"
PASSWORD = "admin123"

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/auth', methods=['POST'])
def auth():
    user = request.form['username']
    pwd = request.form['password']

    if user == USERNAME and pwd == PASSWORD:
        return redirect(url_for('dashboard'))
    else:
        return "Invalid Credentials ❌"

@app.route('/dashboard')
def dashboard():
    return render_template("index.html")
@app.route('/scan')
def scan():
    return {"vulnerabilities": 1, "status": "Warning"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)