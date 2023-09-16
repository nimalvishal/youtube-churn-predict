from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == '123@123' and password == '123456':
        return redirect(url_for('onscreen'))
    else:
        return 'INVALID!'

@app.route('/onscreen')
def onscreen():
    return render_template('onscreen.html')

if __name__ == '__main__':
    app.run(debug=True)
