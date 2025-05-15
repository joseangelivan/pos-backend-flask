import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://app_user:6TwkGlkkbq7f71iNS6bgYKrTn4LA8LDA@dpg-d0j0os95pdvs739uh8gg-a/app_db_v4pz
')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
