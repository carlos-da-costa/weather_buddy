from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

DEBUG = environ['DEBUG']
CACHE_TYPE = "FileSystemCache"
CACHE_DEFAULT_TIMEOUT = int(environ['CACHE_DEFAULT_TIMEOUT'])
CACHE_DIR = environ["CACHE_DIR"]
CACHE_SIZE = int(environ["CACHE_SIZE"])
API_KEY = environ['API_KEY']