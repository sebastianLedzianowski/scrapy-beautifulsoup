import requests
from bs4 import BeautifulSoup
from mongodb.models import Quote
from mongodb.tools_file_and_mongodb import save_to_database, save_to_file
from mongodb.connect import connect_mongodb


def web_scraping_quote(url, page_number):
    url_with_page = f"{url}/page/{page_number}/"
    response = requests.get(url_with_page)
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    quote_list = []

    for i in range(0, len(quotes)):
        quote_text = quotes[i].text
        author_name = authors[i].text
        tagsforquote = tags[i].find_all('a', class_='tag')
        tag_list = [tag.text for tag in tagsforquote]

        quote_data = {
            "quote": quote_text,
            "author": author_name,
            "tags": tag_list
        }
        quote_list.append(quote_data)

    return quote_list


if __name__ == "__main__":
    connect_mongodb()
    url = 'http://quotes.toscrape.com'

    quotes_database = []
    for page_number in range(1, 11):
        quotes = web_scraping_quote(url, page_number)
        for quote_data in quotes:
            new_quote = {
                'quote': quote_data['quote'],
                'author': quote_data["author"],
                'tags': quote_data['tags']
            }
            quotes_database.append(new_quote)
            save_to_database(Quote, new_quote)
    save_to_file(quotes_database, 'quotes_soup.json')
