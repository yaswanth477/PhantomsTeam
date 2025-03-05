from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect


mail = Mail()  # Create a Mail instance but don't bind it yet
csrf = CSRFProtect()