# -*- coding: utf-8 -*-

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import random

class ImgurPipeline(ImagesPipeline):

    def set_filename(self, response):
        my_number = random.randrange(1,100,1)
        #add a regex here to check the title is valid for a filename.
        return 'full/{0}'.format(response.meta['my_nice_file_name']) + '-real-estate-mls-listings-homes-and-condos' + str(my_number) +'.jpg'

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={'my_nice_file_name': item['my_nice_file_name']})

    def get_images(self, response, request, info):
        for key, image, buf in super(ImgurPipeline, self).get_images(response, request, info):
            key = self.set_filename(response)
        yield key, image, buf
