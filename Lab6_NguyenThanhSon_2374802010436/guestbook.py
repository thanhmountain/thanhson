from flask import Flask, render_template, request

app = Flask(__name__)

# Danh sách lưu trữ các thông điệp
guestbook_entries = []

@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        guestbook_entries.append({'name': name, 'message': message})
    
    return render_template('guestbook.html', entries=guestbook_entries)

if __name__ == '__main__':
    app.run(debug=True)
