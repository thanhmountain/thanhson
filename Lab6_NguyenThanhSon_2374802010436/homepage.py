from flask import Flask, render_template

app = Flask(__name__)

# Route hiển thị trang chủ
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Route cho trang About
@app.route('/about')
def about():
    return render_template('about.html')  # Tạo file about.html trong templates

if __name__ == '__main__':
    app.run(debug=True)
