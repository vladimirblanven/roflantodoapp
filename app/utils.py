from app.models import db

def get_first_available_id():
    result = db.session.execute('''
        SELECT id + 1
        FROM todos t
        WHERE NOT EXISTS (
            SELECT 1
            FROM todos t2
            WHERE t2.id = t.id + 1
        )
        ORDER BY id
        LIMIT 1
    ''')
    return result.scalar() or 1

