from flask import Flask, render_template, request

app = Flask(__name__)

# Danh sách nhiệm vụ với trạng thái hoàn thành
tasks = [
    {'task': 'Learn Flask', 'completed': False},
    {'task': 'Build a web app', 'completed': False},
]

@app.route('/todo', methods=['GET', 'POST'])
def todolist():
    if request.method == 'POST':
        new_task = request.form['task']
        tasks.append({'task': new_task, 'completed': False})
    
    # Thay đổi trạng thái hoàn thành của nhiệm vụ
    if 'toggle' in request.form:
        task_index = int(request.form['toggle'])
        tasks[task_index]['completed'] = not tasks[task_index]['completed']
    
    return render_template('todolist.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
