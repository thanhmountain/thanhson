from flask import Flask, render_template

app = Flask(__name__)

@app.route('/math')
def math():
    # Các phép toán cơ bản
    result = {
        'addition': 5 + 3,
        'subtraction': 5 - 3,
        'multiplication': 5 * 3,
        'division': 5 / 3
    }
    return render_template('math.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
