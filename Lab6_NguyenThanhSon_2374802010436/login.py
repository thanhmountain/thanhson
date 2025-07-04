from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Tạo một danh sách người dùng giả lập
users = {
    'admin': 'password123',
    'user': 'mypassword'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Kiểm tra thông tin đăng nhập
        if username in users and users[username] == password:
            return redirect(url_for('welcome', username=username))
        else:
            return 'Invalid credentials, please try again.'
    
    return render_template('login.html')

@app.route('/welcome/<username>')
def welcome(username):
    return f'Welcome, {username}! You have successfully logged in.'

if __name__ == '__main__':
    app.run(debug=True)
