import pymongo
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
load_dotenv()

mongodb_password = os.environ['mongodb_password']
mongodb_password = quote_plus(mongodb_password)

connect_string = f'mongodb+srv://hdttuan:{mongodb_password}@cluster0.h09da4d.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(connect_string)
client = client['TRACKINGINVESTMENT_CRAWL']



