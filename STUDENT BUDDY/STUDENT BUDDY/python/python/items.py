# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ListingItem(scrapy.Item):
    project_name = scrapy.Field()
    urls = scrapy.Field()