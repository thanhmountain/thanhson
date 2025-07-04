from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/newfile', methods=['GET', 'POST'])
def newfile():
    message = ''
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        user_input = request.form['user_input']
        message = f'You entered: {user_input}'
    
    return render_template('newfile.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
