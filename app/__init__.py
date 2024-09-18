from flask import Flask
from flask_mail import Mail, Message
from pymongo import MongoClient
from .tasks import celery

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Setup MongoDB
    mongo_client = MongoClient(app.config['MONGO_URI'])
    app.db = mongo_client.get_default_database()

    celery.conf.update(app.config)

    # Initialize Flask-Mail
    mail = Mail(app)

    # Send a test email when the app starts
    with app.app_context():
        send_test_email(mail)

    @app.route('/')
    def hello():
        return "Hello, World!"

    return app

# Function to send test email
def send_test_email(mail):
    try:
        msg = Message("Test Email", recipients=["tejasmahajan117@gmail.com"])
        msg.body = "This is a test email sent on app startup."
        mail.send(msg)
        print("Test email sent successfully.")
    except Exception as e:
        print(f"Failed to send test email: {e}")