from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Define the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Connect to the database and check if the user exists
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        result = c.fetchone()

        if result:
            # If the user exists, store the username in the session
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            # If the user doesn't exist, display an error message
            error = 'Invalid username or password'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Define the dashboard route
@app.route('/dashboard')
def dashboard():
    # Get the username from the session
    username = session.get('username')
    if not username:
        # If the username is not in the session, redirect to the login page
        return redirect(url_for('login'))

    return render_template('dashboard.html', username=username)

# Define the logout route
@app.route('/logout')
def logout():
    # Clear the username from the session
    session.pop('username', None)
    return redirect(url_for('login'))
