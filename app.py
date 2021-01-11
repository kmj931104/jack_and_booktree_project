from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_jack_and_beantree():
    return render_template('index.html')

@app.route('/books')
def book_tree_current():
    return render_template('booktree_page.html')

@app.route('/books/add')
def book_tree_adding():
    return render_template('booktree_add.html')

@app.route('/booktree')
def book_tree_now():
    return render_template('beanTree.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
