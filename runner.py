import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    host = os.getenv('FLASK_RUN_HOST')
    port = int(os.getenv('FLASK_RUN_PORT'))
    app.run(host=host, port=port)
