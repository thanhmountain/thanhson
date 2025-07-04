from flask import Flask, render_template
import random

app = Flask(__name__)

# Danh sách các trích dẫn
quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Your time is limited, so don't waste it living someone else's life."
]

@app.route('/quote')
def quote():
    random_quote = random.choice(quotes)  # Chọn một trích dẫn ngẫu nhiên
    return render_template('quote.html', quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True)
