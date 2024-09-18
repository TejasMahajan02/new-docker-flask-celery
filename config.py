import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/mydb')
    CELERY_BROKER_URL = os.environ.get(
        'CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.environ.get(
        'CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
