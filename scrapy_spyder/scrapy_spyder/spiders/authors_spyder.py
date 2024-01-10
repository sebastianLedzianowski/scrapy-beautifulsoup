from urllib.parse import urljoin

import scrapy
from scrapy.crawler import CrawlerProcess


class AuthorsSpider(scrapy.Spider):
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors.json"}

    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        author_links = self.author_links(response)
        for author_link in author_links:
            if author_link:
                full_url = urljoin(self.start_urls[0], author_link)
                yield scrapy.Request(url=full_url, callback=self.parse_author)

        next_link = self.next_link(response)
        if next_link:
            full_next_url = urljoin(self.start_urls[0], next_link)
            yield scrapy.Request(url=full_next_url, callback=self.parse)

    def author_links(self, response):
        author_links = response.xpath(
            "//span[@class='text']/following-sibling::span/small[@class='author']/following-sibling::a[@href]/@href").getall()
        return author_links

    def next_link(self, response):
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        return next_link

    def parse_author(self, response):
        fullname = response.xpath("//h3[@class='author-title']/text()").extract_first()
        born_date = response.xpath("//span[@class='author-born-date']/text()").extract_first()
        born_location = response.xpath("//span[@class='author-born-location']/text()").extract_first()
        description = response.xpath("//div[@class='author-description']/text()").get()

        yield {
            "fullname": fullname,
            "born_date": born_date,
            "born_location": born_location[3:],
            "description": description
        }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(AuthorsSpider)
    process.start()
