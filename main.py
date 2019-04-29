from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
        'title': 'My First Post',
        'content': 'This is the first post content!!',
        'author': 'Rahman Fadhil',
        'created_at': 'January 14, 2019'
    },
    {
        'title': 'My Second Post',
        'content': 'This is the second post content!!',
        'author': 'Chris Hemsworth',
        'created_at': 'May 20, 2019'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='Home Page')


if __name__ == "__main__":
    app.run(debug=True)
