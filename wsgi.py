import os
from app.routes.main import app

if __name__ == '__main__':
    app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY",'123')
    app.run(host="0.0.0.0",port=5000)