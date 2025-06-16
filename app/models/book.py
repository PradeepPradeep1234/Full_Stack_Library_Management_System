from app import db

class Add_Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Book_Name = db.Column(db.String(100), nullable=False)
    Author_Name = db.Column(db.String(100), nullable=False)
    Status = db.Column(db.String(20), nullable=False)
    Book_id = db.Column(db.Integer, nullable=False)
    Genre_type = db.Column(db.String(100), nullable=False)
