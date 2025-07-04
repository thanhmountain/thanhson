from flask import Flask, render_template, request

app = Flask(__name__)

# Danh sách nhiệm vụ (các nhiệm vụ sẽ được lưu trong một danh sách)
tasks = []

@app.route('/tasks', methods=['GET', 'POST'])
def tasklist():
    if request.method == 'POST':
        new_task = request.form['task']
        tasks.append(new_task)  # Thêm nhiệm vụ mới vào danh sách
    
    return render_template('tasklist.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
