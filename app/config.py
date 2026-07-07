import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'gamefinder-dev-key')

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'gamefinder')

USD_TO_IDR = 16000
