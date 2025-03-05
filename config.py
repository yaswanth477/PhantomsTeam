import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'phantomsxi.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True

    # Flask-Mail Configuration
    MAIL_SERVER = "smtp.gmail.com"  # Use your email provider's SMTP server
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "teamphantomscc@gmail.com"  # Replace with your email
    MAIL_PASSWORD = "ugel aoiu iwpu woih"  # Use an app password if needed
    MAIL_DEFAULT_SENDER = "teamphantomscc@gmail.com"
