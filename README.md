# Scrapy BeautifulSoup Web Scraping Project 🕷️📜

This project is a web scraping application using Scrapy and BeautifulSoup to collect quotes and author information from the [quotes.toscrape.com](https://quotes.toscrape.com) website. The data is then stored in both JSON files and a MongoDB database.



## Table of Contents 📚

- [Prerequisites 🛠️](#prerequisites)
- [Installation ⬇️](#installation)
- [Configuration ⚙️](#configuration)
- [Usage 🚀](#usage)
- [Project Structure 📁](#project-structure)
- [Created 👤](#created)
- [License 📄](#license)

## Prerequisites 🛠️

Make sure you have the following installed on your machine:

- Python 3.11
- [MongoDB](https://www.mongodb.com/try/download/community)

## Installation ⬇️

1.Clone the repository:

```bash
git clone https://github.com/sebastianLedzianowski/web-scraping.git
```

2.Navigate to the Project Directory:

```bash
cd web-scraping
```

3.Set up a virtual environment and activate it (optional but recommended):

```bash
virtualenv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4.Install dependencies using Poetry:

```bash
pip install poetry
poetry install
```

## Configuration ⚙️

To run this project, you will need to add the following environment variables to your `.env` file.

```bash
# MongoDB settings
DB_HOST=
DB_DB=
```
---

**Note**: Ensure to keep your `.env` file secure and never commit it to the repository to protect sensitive information.

---

## Usage 🚀

1.Run the web scraping script to collect quotes and author information:

```bash
python quotes_spider.py
python authors_spider.py
python quotes_soup.py
python authors_soup.py
```

2.Check the generated JSON files:

`quotes_spyder.json`, `authors_spyder.json` and `quotes_soup.json`, `quotes_soup.json`

3.Import scraped data into MongoDB:

```bash
python import_to_mongodb.py
```

The `import_to_mongodb` script reads data from the Scrapy and BeautifulSoup JSON files and imports it into MongoDB. Make sure to configure the MongoDB connection details in the `.env` file.


## Project Structure 📁

- **mongodb/**
  - `connect.py`: Module for connecting to MongoDB.
  - `models.py`: MongoDB models for Quote and Author.
  - `tools_file_and_mongodb.py`: Tools for handling file I/O and MongoDB operations.

- **scrapy_spyder/**
  - **scrapy_spyder/**
    - **spiders/**: Directory containing Scrapy spider scripts.
      - `quotes_spyder.py`: Scrapy spider for collecting quotes.
      - `quotes_spyder.json`: JSON file containing quotes prased using scrapy_spyder.
      - `authors_spyder.py`: Scrapy spider for collecting authors.
      - `authors_spyder.json`: JSON file containing quotes prased using scrapy_spyder.

- **beautifulsoup/**
  - `quotes_soup.py`: BeautifulSoup for collecting quotes.
  - `quotes_soup.json`: JSON file containing quotes scraped using BeautifulSoup.
  - `authors_soup.py`: BeautifulSoup for collecting authors.
  - `authors_soup.json`: JSON file containing author information scraped using BeautifulSoup.

- **.env**: Environment variables file with MongoDB connection details.
- **poetry.lock**: Poetry lock file.
- **pyproject.toml**: Poetry project file.
- **import_to_mongodb.py**: Script for importing scraped data into MongoDB.
- **README.md**: Project documentation.
- **LICENSE**: The license file specifying the terms under which the project is distributed.



## Created 👤

- [Sebastian Ledzianowski](https://github.com/sebastianLedzianowski)


## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
