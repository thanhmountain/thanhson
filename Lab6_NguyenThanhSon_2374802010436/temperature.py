from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    result = ''
    if request.method == 'POST':
        temp = float(request.form['temperature'])
        convert_type = request.form['convert_type']

        if convert_type == 'CtoF':
            result = (temp * 9/5) + 32  # Celsius to Fahrenheit
        elif convert_type == 'FtoC':
            result = (temp - 32) * 5/9  # Fahrenheit to Celsius

    return render_template('temperature.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
