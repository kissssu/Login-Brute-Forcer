#!/usr/bin/python3

from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret123'  # Required for session cookies

# Route for login page
@app.route('/')
def index():
    return render_template('login.html')  # Render login form

# Route to handle login POST request
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Dummy check for username and password
    if username == 'admin' and password == 'password':
        # Create a response and set a cookie
        response = make_response(redirect(url_for('success')))
        response.set_cookie('username', username)
        return response
    else:
        return "Invalid credentials", 401

# Route to display success message
@app.route('/success')
def success():
    username = request.cookies.get('username')
    if username:
        return f'Welcome, {username}!'
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
