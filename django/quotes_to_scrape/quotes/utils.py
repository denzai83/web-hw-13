from pymongo import MongoClient


def get_mongodb():
    client = MongoClient('mongodb+srv://hw8:567432@cluster0.g08jtiw.mongodb.net/test')
    db = client.hw10
    return db