import logging

from mongodb.connect import connect_mongodb
from mongodb.models import Quote, Author
from mongodb.tools_file_and_mongodb import open_file, save_to_database

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s')
    connect_mongodb()

    data_base_spyder_quote = open_file('scrapy_spyder/scrapy_spyder/spiders/quotes_spyder.json')
    for data in data_base_spyder_quote:
        save_to_database(Quote, data)

    data_base_spyder_author = open_file('scrapy_spyder/scrapy_spyder/spiders/authors_spyder.json')
    for data in data_base_spyder_author:
        save_to_database(Author, data)

    data_base_soup_quote = open_file('beautifulsoup/quotes_soup.json')
    for data in data_base_soup_quote:
        save_to_database(Quote, data)

    data_base_soup_author = open_file('beautifulsoup/authors_soup.json')
    for data in data_base_soup_author:
        save_to_database(Author, data)