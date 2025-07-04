from flask import Flask, render_template

app = Flask(__name__)

# Biến toàn cục để theo dõi số lần truy cập
visit_count = 0

@app.route('/counter')
def counter():
    global visit_count
    visit_count += 1  # Tăng số lần truy cập lên 1
    return render_template('counter.html', visit_count=visit_count)

if __name__ == '__main__':
    app.run(debug=True)
