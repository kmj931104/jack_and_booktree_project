from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient


app = Flask(__name__)


@app.route('/')
def home_jack_and_beantree():
    return render_template('index.html')

# @app.route('/books')
# def book_tree_current():
#     return render_template('booktree_page.html')

@app.route('/books', methods=['GET'])
def book_tree_adding():
    return render_template('booktree_add.html')

def book_added():
    title = request.form['title'];
    author = request.form['author'];
    page = request.form['title'];
    isbn = request.form['isbn'];
    sentence = request.form['sentence'];
    comment = request.form['comment'];
    date = request.form['date'];
    rate =request.form['rate'];

    print(title, author, page, isbn, sentence, comment, date, rate);

@app.route('/booktree')
def book_tree_now():
    return render_template('beanTree.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
