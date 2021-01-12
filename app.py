from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup

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


@app.route('/booksadd/search', methods=['POST'])
def searching_book_info():
    isbn = request.form['isbn']

    url = 'https://www.aladin.co.kr/shop/wproduct.aspx?ISBN=' + isbn

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    image = soup.select_one('#CoverMainImage').get("src")
    title = soup.select_one(
        '#Ere_prod_allwrap > div.Ere_prod_topwrap > div.Ere_prod_titlewrap > div.left > div > ul > li:nth-child(1) > div > a.Ere_bo_title').text
    author = soup.select_one(
        '#Ere_prod_allwrap > div.Ere_prod_topwrap > div.Ere_prod_titlewrap > div.left > div > ul > li.Ere_sub2_title > a:nth-child(1)').text
    page = soup.select_one(
        '#Ere_prod_allwrap > div.Ere_prod_middlewrap > div:nth-child(1) > div.Ere_prod_mconts_R > div.conts_info_list1 > ul > li:nth-child(1)').text


    info = {
        'image': image,
        'title': title,
        'author': author,
        'page': page
    }

    db.bookinfo.insert_one(info)

    return jsonify({'result': 'success', 'msg': '책 정보 가져오기 성공!'})


@app.route('/booktree')
def book_tree_now():
    return render_template('beanTree.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
