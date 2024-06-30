from sqlalchemy import text
from app.extensions import db

def get_first_available_id():
    result = db.session.execute(text('SELECT id FROM todos ORDER BY id'))
    all_ids = [row[0] for row in result]

    if not all_ids:
        return 1

    for i in range(1, max(all_ids) + 2):
        if i not in all_ids:
            return i
