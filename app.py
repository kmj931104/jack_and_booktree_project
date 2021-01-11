from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home_jack_and_booktree():
    return render_template('index.html')


@app.route('/booksadd')
def book_tree_add():
    return render_template('booktree_add.html')


@app.route('/booksadd', methods=['POST'])
def adding_book_tree():
    title = request.form['title']
    author = request.form['author']
    page = request.form['page']
    isbn = request.form['isbn']
    sentence = request.form['sentence']
    comment = request.form['comment']
    date = request.form['date']
    rate = request.form['rate']

    doc = {
        'title': title,
        'author': author,
        'page': page,
        'isbn': isbn,
        'sentence': sentence,
        'comment': comment,
        'date': date,
        'rate': rate
    }

    db.booktree.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '잭의 책나무가 한뼘 자라났습니다!'})


@app.route('/booktree')
def book_tree_now():
    return render_template('beanTree.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
