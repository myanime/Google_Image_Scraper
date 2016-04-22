# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from image_scraper.items import HousePicture
import scrapy
import time
import string
from scrapy.http import FormRequest
from scrapy.item import Item, Field
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from selenium import webdriver


class MyHouseSpider(scrapy.Spider):
    name = "my-house-spider"
    start_urls = ["https://www.google.com/search?q=utah+homes&tbs=isz:lt%2Cislt:4mp&tbm=isch"]
    number_of_pictures_to_scrape = 5
    def parse(self, response):
        #city_urls = ["https://www.google.com/search?q=utah+homes&tbs=isz:lt%2Cislt:4mp&tbm=isch", "https://www.google.com/search?q=dogs&tbs=isz:lt%2Cislt:4mp&tbm=isch"]
        city_urls = ["homes-utah", "dogs-furry"]
        driver = webdriver.Firefox()
        picture_array = []
        for city_number in range(0,len(city_urls)):
            i = 1
            while i < self.number_of_pictures_to_scrape:
                try:
                    search_string = string.replace(city_urls[city_number], '-', '+') 
                    driver.get("https://www.google.com/search?q=" + search_string + "&tbs=isz:lt%2Cislt:4mp&tbm=isch")
                    picture_url = driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[" +str(i) + "]/a").get_attribute("href")
                    picture_url = picture_url.split('http://images.google.de/imgres?imgurl=', 1)[1]
                    picture_url = picture_url.split('&imgrefurl', 1)[0]
                    picture_array.append(picture_url)
                    i = i + 1
                except:
                    i = i + 1                    
            for x in range(0, len(picture_array)):
                yield HousePicture(image_urls=[picture_array[x]], my_nice_file_name="google")
