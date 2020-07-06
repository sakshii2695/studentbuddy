# -*- coding: utf-8 -*-
import scrapy
from python.items import ListingItem

class PythonspiderSpider(scrapy.Spider):
    name = 'pythonspider'
    
    start_urls = ['https://code-projects.org/c/languages/project/pythonprojects/']
        
    def parse(self, response):
        item=ListingItem()
        self.log('i have visited:' + response.url)
        item['project_name'] = response.xpath('//div[@class = "st-loop-entry-content st-clr"]/header/h2/a/text()').extract()[0]
        item['urls'] =  response.xpath('//div[@class = "st-loop-entry-content st-clr"]/header/h2/a/@href').extract()[0]
        print(item)
        yield(item)
           
           
           # for pro in response.css('div.st-loopentry-inner st-clr'):