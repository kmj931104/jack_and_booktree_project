from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bson.objectid import ObjectId

import datetime

client = MongoClient('mongodb://kmj:duqhtkfkdgo@13.209.19.24', 27017)
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

    date = datetime.datetime.strptime(date, '%Y-%m-%d')

    image = "https://cdn.pixabay.com/photo/2019/03/18/15/23/fantasies-4063346_960_720.jpg"

    try:
        url = 'https://www.aladin.co.kr/shop/wproduct.aspx?ISBN=' + isbn

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')

        image = soup.select_one('#CoverMainImage').get("src")

    except Exception:
        pass


    book = {
        'image': image,
        'title': title,
        'author': author,
        'page': page,
        'isbn': isbn,
        'sentence': sentence,
        'comment': comment,
        'date': date,
        'rate': rate
    }
    db.booktree.insert_one(book)

    return jsonify({'result': 'success', 'msg': '잭의 책나무가 한뼘 자라났습니다!'})


@app.route('/beantree', methods=["GET"])
def books_info():

    infos = list(db.booktree.find().sort('date', -1))

    for info in infos:
        info['_id'] = str(info['_id'])
        info['date'] = info['date'].strftime('%Y-%m-%d')

    return jsonify({'result':'success', 'infos':infos})

@app.route('/booktree/one', methods=['GET'])
def get_one_booktree():
    bookId = request.args.get('bookId')
    book = db.booktree.find_one({'_id': ObjectId(bookId)})
    book['_id'] = str(book['_id'])
    book['date'] = book['date'].strftime('%Y-%m-%d')
    return jsonify({'result':'success', 'book': book})


@app.route('/booktree')
def book_tree_now():
    return render_template('beanTree.html')


@app.route('/bookregister')
def book_tree_register():
    return render_template('booktree_now.html')



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
