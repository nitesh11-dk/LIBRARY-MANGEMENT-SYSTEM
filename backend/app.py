# app.py
from flask import Flask
from flask_cors import CORS
from init_db import init_db 
from routes.user_routes import user_bp
from routes.book_routes import book_bp
from flask_session import Session


app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Initialize SQLite database with tables
init_db()

# Register the Blueprints
app.register_blueprint(user_bp)
app.register_blueprint(book_bp)



# Configure the session to use the filesystem (or Redis, or other backends)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'Nitesh_DK_1234'  # Replace with your own secret key
Session(app)

if __name__ == '__main__':
    app.run(debug=True)
