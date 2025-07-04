from flask import Flask, render_template

app = Flask(__name__)

# Dữ liệu các câu hỏi và câu trả lời
faq = {
    1: {'question': 'What is Flask?', 'answer': 'Flask is a web framework for Python.'},
    2: {'question': 'How do I install Flask?', 'answer': 'You can install Flask with pip: pip install flask.'},
}

@app.route('/faq/<int:question_id>')
def faq_page(question_id):
    question = faq.get(question_id)
    if question is None:
        return "Question not found", 404
    return render_template('faq.html', question=question)

if __name__ == '__main__':
    app.run(debug=True)
