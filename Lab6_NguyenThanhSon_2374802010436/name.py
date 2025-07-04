from flask import Flask, render_template, request

app = Flask(__name__)

# Route hiển thị form nhập tên
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']  # Nhận tên từ form
        return render_template('success.html', name=name)  # Trả về trang success.html với tên người dùng
    return render_template('name.html')  # Render form khi là GET request

if __name__ == '__main__':
    app.run(debug=True)
