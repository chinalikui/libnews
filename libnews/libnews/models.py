from app import db

lass New(db.Model):
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

