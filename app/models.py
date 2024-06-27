from app.extensions import db
from datetime import datetime
import pytz

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75), nullable=False)
    description = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }
