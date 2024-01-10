import requests
from bs4 import BeautifulSoup
import re

from mongodb.models import Author
from mongodb.tools_file_and_mongodb import save_to_database, save_to_file
from mongodb.connect import connect_mongodb


def get_author_link(url, page_number):
    url_with_page = f"{url}/page/{page_number}/"
    response = requests.get(url_with_page)
    soup = BeautifulSoup(response.text, 'lxml')
    authors_links = soup.find_all('a', href=re.compile(r"/author/"))
    links = [author['href'] for author in authors_links]

    return links


def web_scraping_authors(url, authors_link):
    url_with_page = f"{url}{authors_link}"
    response = requests.get(url_with_page)
    soup = BeautifulSoup(response.text, 'lxml')

    fullname = soup.find_all('h3', class_='author-title')
    born_date = soup.find_all('span', class_='author-born-date')
    born_location = soup.find_all('span', class_='author-born-location')
    description = soup.find_all('div', class_='author-description')

    author_list = []

    for i in range(0, len(fullname)):
        fullname_text = fullname[i].text
        born_date_text = born_date[i].text
        born_location_text = born_location[i].text
        description_text = description[i].text

        author_date = {
            "fullname": fullname_text,
            "born_date": born_date_text,
            "born_location": born_location_text,
            "description": description_text
        }
        author_list.append(author_date)

    return author_list


if __name__ == "__main__":
    connect_mongodb()
    url = 'http://quotes.toscrape.com'
    link_authors = []

    for page_number in range(1, 11):
        authors = get_author_link(url, page_number)
        link_authors.extend(authors)

    authors_link_set = set(link_authors)
    unique_authors_link = list(authors_link_set)

    authors_database = []
    for author_link in unique_authors_link:
        authors = web_scraping_authors(url, author_link)

        for author_date in authors:
            new_authors = {
                'fullname': author_date['fullname'],
                'born_date': author_date['born_date'],
                'born_location': author_date['born_location'],
                'description': author_date['description']
            }
            authors_database.append(new_authors)
            save_to_database(Author, new_authors)
    save_to_file(authors_database, 'beautifulsoup/authors_soup.json')
