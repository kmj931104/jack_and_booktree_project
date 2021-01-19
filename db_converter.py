from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.dbsparta

for item in db.booktree.find():
    if 'date' in item:
        item['date'] = datetime.datetime.strptime(item['date'], '%Y-%m-%d')
        db.booktree.replace_one({'_id': item['_id']}, item)