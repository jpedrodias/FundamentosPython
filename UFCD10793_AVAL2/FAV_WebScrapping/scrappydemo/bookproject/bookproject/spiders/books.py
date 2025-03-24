'''
Exercício 2 - FAV Enunciado WebScraping - Scrapy 
'''

import csv
import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        URL = 'http://books.toscrape.com/'
        yield scrapy.Request(url=URL, callback=self.response_parser)
    
    def response_parser(self, response):
        for selector in response.css('article.product_pod'):
            yield {
                'title': selector.css('h3 > a::attr(title)').extract_first(),
                'price': selector.css('.price_color::text').extract_first()
            }
        
        next_page_link = response.css('li.next > a::attr(href)').extract_first()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)
    
#end class

def book_spider_result():
    books_results= []

    def crawler_results(item):
        books_results.append(item)
    
    dispatcher.connect(crawler_results, signal=signals.item_scraped) 
    crawler_process = CrawlerProcess() 
    crawler_process.crawl(BooksSpider) 
    crawler_process.start() 
    return books_results 
#end def

if __name__ == '__main__':
    books = book_spider_result()
    with open('books.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'price'])
        writer.writeheader()
        writer.writerows(books)
