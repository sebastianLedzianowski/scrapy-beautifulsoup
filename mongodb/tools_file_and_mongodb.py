import json
import logging
import os
from typing import Type, Union, Dict, Any

from mongoengine import DoesNotExist
from mongodb.models import Quote, Author


def open_file(document: str) -> Union[Dict[str, Any], None]:
    if os.path.exists(document):
        try:
            with open(document, 'r') as file:
                document_data = json.load(file)
                logging.info("The document is opened.")
                return document_data
        except Exception as e:
            return logging.warning(f'Document not opened: {e}')
    else:
        return logging.info(f'Document not found: {document}')


def save_to_file(data: Union[Dict[str, Any]], filepath: str) -> bool:
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f'The data has been saved to a file: {filepath}')
        return True
    except Exception as e:
        logging.error(f'An error occurred while writing to the file {filepath}: {e}')
        return False


def text_exists(model: Type[Union[Quote, Author]], text_to_check: str) -> bool:
    try:
        if model == Quote:
            existing_text = Quote.objects.get(quote=text_to_check)
        elif model == Author:
            existing_text = Author.objects.get(fullname=text_to_check)
        logging.info(f'Text exists in the database for {model.__name__}: {text_to_check}')
        return True
    except DoesNotExist as e:
        logging.info(f'Text does not exist in the database for {model.__name__}: {text_to_check}')
        return False
    except Exception as e:
        logging.error(f'An error occurred while checking text existence: {e}')
        return False


def save_to_database(model: Type[Union[Quote, Author]], data: Union[Dict[str, Any]]) -> None:
    try:
        text_to_save = data['quote'] if model == Quote else data['fullname']
        if not text_exists(model, text_to_save):
            new_data = model(**data)
            new_data.save()
            logging.info(f"Added new data to database: {text_to_save}")
        else:
            logging.info(f"Data already exists in database: {text_to_save}")
    except KeyError as e:
        logging.error(f"KeyError: {e}. Check if the required fields are present in the data.")
