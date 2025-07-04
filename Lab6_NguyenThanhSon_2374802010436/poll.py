from flask import Flask, render_template, request

app = Flask(__name__)

# Lưu trữ kết quả của cuộc khảo sát
poll_options = ['Cats', 'Dogs', 'Birds']
votes = {'Cats': 0, 'Dogs': 0, 'Birds': 0}

@app.route('/poll', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        choice = request.form['vote']
        if choice in votes:
            votes[choice] += 1
    
    total_votes = sum(votes.values())
    percentages = {option: (votes[option] / total_votes * 100) if total_votes > 0 else 0 for option in votes}
    
    return render_template('poll.html', options=poll_options, votes=votes, percentages=percentages)

if __name__ == '__main__':
    app.run(debug=True)
