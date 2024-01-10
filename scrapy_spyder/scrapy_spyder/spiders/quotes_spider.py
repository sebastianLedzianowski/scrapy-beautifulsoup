from urllib.parse import urljoin

import scrapy
from scrapy.crawler import CrawlerProcess


class QuotesSpider(scrapy.Spider):
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "quotes.json"}

    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'tags': quote.xpath("div[@class='tags']/a/text()").extract(),
                'author': quote.xpath("span/small/text()").extract_first(),
                'quote': quote.xpath("span[@class='text']/text()").get()
            }

        next_link = self.next_link(response)
        if next_link:
            full_next_url = urljoin(self.start_urls[0], next_link)
            yield scrapy.Request(url=full_next_url, callback=self.parse)

    def next_link(self, response):
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        return next_link


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()
