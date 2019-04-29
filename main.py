from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
        'title': 'My First Post',
        'content': 'This is the first post content!!'
    },
    {
        'title': 'My Second Post',
        'content': 'This is the second post content!!'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
