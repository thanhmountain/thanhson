from flask import Flask, render_template

app = Flask(__name__)

@app.route('/score')
def score():
    # Danh sách điểm các môn học
    scores = {
        'Math': 95,
        'Science': 88,
        'English': 92,
        'History': 85
    }
    
    # Tính điểm trung bình
    average_score = sum(scores.values()) / len(scores)
    
    return render_template('score.html', scores=scores, average_score=average_score)

if __name__ == '__main__':
    app.run(debug=True)
