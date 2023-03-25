from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

posts = {
    0: {
        'post_id' : 0,
        'title': 'Hello world',
        'content': 'This is my first blog post'
    }
}


@app.route('/')
def home():
    return render_template('home.html' , posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return 'There is nothing to show'
    return render_template('post.html', post=post)


@app.route('/shop/')
def shop():
    return 'Hello aku'


@app.route('/post/form')
def form():
    return render_template('create.html')


@app.route('/post/create', methods=['post'])
def create():
    title = request.form.get('title')
    content = request.form.get('content')

    post_id = len(posts)
    posts[post_id] = {'id': post_id, 'title': title, 'content': content}

    return redirect(url_for('post', post_id=post_id))


if __name__ == '__main__':
    app.run(debug=True)
