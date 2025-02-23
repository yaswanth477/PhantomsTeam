from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    batting_avg = db.Column(db.Float, nullable=False)
    wickets = db.Column(db.Integer, nullable=True)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opponent = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    result = db.Column(db.String(50), nullable=True)
