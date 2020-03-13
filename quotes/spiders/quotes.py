# -*- coding: utf-8 -*-
from scrapy.utils.response import open_in_browser
from scrapy import Spider
from scrapy.http import FormRequest, Request
from quotes.items import ProjectItem
import pymongo
from quotes.helpers.auth import AuthEncrypt


class QuotesSpider(Spider):
    name = 'quotes'
    start_urls = ('http://quotes.toscrape.com/login',)

    def __init__ (self):
        self.conn = pymongo.MongoClient(
           "mongodb+srv://write_user:write_pass@futebol-iwbwh.mongodb.net/test?retryWrites=true&w=majority",
            27017
        )

        db = self.conn['test']
        self.collection = db['auth']

    def parse(self, response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()

        result = self.collection.find_one({}, {"_id": 0})
        auth = AuthEncrypt()
        password = auth.decrypt_password(password=result['password'])
        username = result.get('username')

        return FormRequest.from_response(response=response,
                                         formdata={
                                             'csrf_token': token,
                                             'username': username,
                                             'password': password,
                                         },
                                         callback=self.scrape_pages)

    def scrape_pages(self, response):
        """
        This function parses a sample response from Quotes page.

        @url http://quotes.toscrape.com/
        @returns items 0 10
        @scrapes text author tags
        """
        item = ProjectItem()

        for quote in response.xpath('//div[@class="quote"]'):
            item['text'] = quote.xpath('./span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath('.//small[@class="author"]/text()').extract_first()
            item['tags'] = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()

            yield item

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:

            yield Request(url=response.urljoin(next_page_url),
                          callback=self.scrape_pages)