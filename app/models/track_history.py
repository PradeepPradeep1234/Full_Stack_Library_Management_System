from app import db
from datetime import datetime

class TrackHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    book_name = db.Column(db.String(100), nullable=False)
    author_name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    action = db.Column(db.String(20), nullable=False)  # borrow or return
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
