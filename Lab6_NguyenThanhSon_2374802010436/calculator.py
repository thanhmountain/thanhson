from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    result = ''
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Error: Division by zero'

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
