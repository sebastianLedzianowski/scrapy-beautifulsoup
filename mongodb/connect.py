import os
from dotenv import load_dotenv
from mongoengine import connect

def connect_mongodb():
    load_dotenv()
    try:
        connect(
            host=os.dotenv('DB_HOST'),
            db=os.dotenv('DB_DB'),
            ssl=True,
        )
        print('Connection to MongoDB successful.')
    except ConnectionError as e:
        print(f'Error connecting to MongoDB: {e}')