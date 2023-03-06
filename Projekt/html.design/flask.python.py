from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    # TODO: validate user's credentials
    if username == 'myusername' and password == 'mypassword':
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'})

if __name__ == '__main__':
    app.run()

