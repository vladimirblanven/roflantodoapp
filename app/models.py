from app.extensions import db, ma
from datetime import datetime
import pytz

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75), nullable=False)
    description = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(pytz.utc))

class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        include_fk = True
        load_instance = True
