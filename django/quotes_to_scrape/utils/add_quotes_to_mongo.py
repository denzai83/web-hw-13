import json
from bson.objectid import ObjectId

from pymongo import MongoClient


client = MongoClient('mongodb+srv://hw8:567432@cluster0.g08jtiw.mongodb.net/test')

db = client.hw10

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)
    
for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'tags': quote['tags'],
            'author': ObjectId(author['_id']),
            'quote': quote['quote']
        })