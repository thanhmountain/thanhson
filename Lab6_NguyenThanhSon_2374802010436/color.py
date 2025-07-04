from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/color', methods=['GET', 'POST'])
def color():
    color = 'white'  # Mặc định là màu trắng
    if request.method == 'POST':
        color = request.form['color']
    
    return render_template('color.html', color=color)

if __name__ == '__main__':
    app.run(debug=True)
