import logging
import os
from dotenv import load_dotenv
from mongoengine import connect

def connect_mongodb():
    load_dotenv()
    try:
        connect(
            host=os.getenv('DB_HOST'),
            db=os.getenv('DB_DB'),
            ssl=True,
        )
        logging.info('Connection to MongoDB successful.')
    except ConnectionError as e:
        logging.warning(f'Error connecting to MongoDB: {e}')