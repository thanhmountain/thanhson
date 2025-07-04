from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    # Kiểm tra nếu username là 'admin'
    if username == 'admin':
        special_message = "Hello Admin, you have special access!"
    else:
        special_message = f"Welcome to your profile, {username}!"

    return render_template('profile.html', username=username, special_message=special_message)

if __name__ == '__main__':
    app.run(debug=True)
