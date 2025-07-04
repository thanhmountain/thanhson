from flask import Flask, render_template

app = Flask(__name__)

# Dữ liệu menu, với các danh mục và món ăn
menu_items = {
    'drinks': [{'name': 'Coffee', 'price': 2}, {'name': 'Tea', 'price': 1.5}],
    'food': [{'name': 'Burger', 'price': 5}, {'name': 'Pizza', 'price': 7}],
}

@app.route('/menu/<category>')
def menu(category):
    if category not in menu_items:
        return "Category not found", 404
    return render_template('menu.html', category=category, items=menu_items[category])

if __name__ == '__main__':
    app.run(debug=True)
