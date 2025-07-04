from flask import Flask, render_template, abort

app = Flask(__name__)

# Dictionary chứa các bài viết (ID bài viết là khóa)
posts = {
    1: {'title': 'First Post', 'content': 'Hello, world! This is my first post.'},
    2: {'title': 'Second Post', 'content': 'This is another post about Flask.'},
    3: {'title': 'Third Post', 'content': 'Here’s some more content for the blog.'}
}

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if post is None:
        abort(404)  # Nếu không tìm thấy bài viết với ID đó, trả về lỗi 404
    return render_template('blog.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
