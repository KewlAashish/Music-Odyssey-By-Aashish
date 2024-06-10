import os


class Config:
    DATABASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DATABASE_DIR, 'music_odyssey.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False