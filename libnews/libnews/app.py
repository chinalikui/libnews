from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
from config import config

#initial
app = Flask(__name__)
app.config.from_object(config['basic'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#models
class New(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.Date)
    source = db.Column(db.String())
    title = db.column(db.String())
    href = db.column(db.String())
    abstract = db.column(db.String())
    detail = db.column(db.String())

    def __init__(self,date,source,title,href,abstract,detail):
        self.date = date
        self.source = source
        self.title = title
        self.href = href
        self.abstract = abstract
        self.detail = detail

    def __repr__(self):
        return '<id {}>'.format(self.id)

#route

@app.route('/')
def index():
    return "lib news list"

@app.route('/<id>')
def detail(id):
    return "No. {} new detail".format(id)


if __name__ == '__main__':
    app.run()


