from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AnalysisModel(db.Model):
    __tablename__ = 'apiV2'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Date())
    category = db.Column(db.String())
    value = db.Column(db.Integer())

    def __init__(self, timestamp, category, value):
        self.timestamp = timestamp
        self.category = category
        self.value = value

    def __repr__(self):
        return f"{self.timestamp}:{self.category}"
