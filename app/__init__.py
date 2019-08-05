from flask import Flask,render_template
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config["MONGO_URI"] = "mongodb+srv://msanc13:Password1@clustere-56177.mongodb.net/BBALL?retryWrites=true&w=majority"
mongo = PyMongo(app)
from app import routes 