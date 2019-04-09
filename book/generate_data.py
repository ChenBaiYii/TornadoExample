from pymongo import MongoClient


connect = MongoClient("localhost", 27017)

database = connect["bookstore"]
database.books.insert_one({"title": "Programming Collective Intelligence",
                           "subtitle": "Building Smart Web 2.0 Application",
                           "image": "Image Not Found",
                           "author": "anonymous",
                           "date_added": 111111111,
                           "description": "<p>[...]<p/>"
                           })




