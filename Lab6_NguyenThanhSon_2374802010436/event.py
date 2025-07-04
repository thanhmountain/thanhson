from flask import Flask, render_template, request

app = Flask(__name__)

# Danh sách các sự kiện (lưu trữ tên sự kiện và ngày diễn ra)
events = [
    {'name': 'Flask Workshop', 'date': '2025-07-01'},
    {'name': 'Python Conference', 'date': '2025-08-15'}
]

@app.route('/events', methods=['GET', 'POST'])
def events_list():
    if request.method == 'POST':
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        events.append({'name': event_name, 'date': event_date})
    
    return render_template('events.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
