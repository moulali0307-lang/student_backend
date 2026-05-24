from urllib.parse import quote_plus

password = quote_plus("Moulali@7")

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{password}@localhost/student_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False