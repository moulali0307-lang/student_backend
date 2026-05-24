from flask import Flask
from config import Config
from database.db import db
from routes.student_routes import student_bp
from flask_cors import CORS

app = Flask(__name__)

# Load Config
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize Database
db.init_app(app)

# Import Model
from models.student import Student

# Create Tables
with app.app_context():
    db.create_all()

# Register Blueprint
app.register_blueprint(student_bp)

# Main File
if __name__ == "__main__":
    app.run(debug=True)