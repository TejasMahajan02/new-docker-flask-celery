import random
from celery import Celery
from datetime import datetime, timedelta
from flask import current_app as app
from flask_mail import Mail, Message

# Set up Celery
celery = Celery(__name__)

# Midnight task: To run at midnight and schedule tasks for the day
@celery.task
def midnight_task():
    db = app.db
    # Clear old timestamps
    db.timestamps.delete_many({})

    # Generate 3 random times
    timestamps = []
    for _ in range(3):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        timestamps.append({"hour": hour, "minute": minute})
    
    # Store the new timestamps
    db.timestamps.insert_many(timestamps)

    # Schedule mailing tasks at each timestamp
    for ts in timestamps:
        schedule_mailing_task.apply_async(eta=datetime.now().replace(hour=ts['hour'], minute=ts['minute'], second=0))

# Mailing task to send emails at generated times
@celery.task
def schedule_mailing_task():
    # Fetch user email (or multiple users) from the database
    user_email = "tejasmahajan117@gmail.com"
    
    # Send mail
    with app.app_context():
        mail = Mail(app)
        msg = Message('Scheduled Email', recipients=[user_email])
        msg.body = "This is a scheduled email sent at your selected time!"
        mail.send(msg)
