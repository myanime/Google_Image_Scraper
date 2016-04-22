# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HousePicture(scrapy.Item):
    file_urls = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    my_nice_file_name = scrapy.Field()
    #files = scrapy.Field()
    
class ImageScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
