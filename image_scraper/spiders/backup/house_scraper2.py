# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from image_scraper.items import HousePicture
import scrapy
import time

from scrapy.http import FormRequest
from scrapy.item import Item, Field
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from selenium import webdriver

class MyHouseSpider(scrapy.Spider):
    name = "my-house-spider2"
    #start_urls = ["https://www.google.com//imgres?imgurl=http%3A%2F%2Fwww.mcarthurhomes.com%2Fassets%2FSiteMedia%2Fblog_photos%2FIMG_0295m-01.jpg&imgrefurl=http%3A%2F%2Fwww.mcarthurhomes.com%2F2012%2F1%2F7%2F1617&docid=w6hE6uteDLdhqM&tbnid=3ceyCybCEspaxM%3A&w=3072&h=2048&ved=0ahUKEwil0dGOl4DMAhXCqA4KHaCgCBQQMwgdKAAwAA&iact=mrc&uact=8#h=2048&imgrc=3ceyCybCEspaxM%3A&w=3072"]
    #start_urls = ["http://images.google.com/imgres?imgurl=http://www.mcarthurhomes.com/assets/SiteMedia/blog_photos/IMG_0295m-01.jpg&imgrefurl=http://www.mcarthurhomes.com/2012/1/7/1617&docid=w6hE6uteDLdhqM&tbnid=3ceyCybCEspaxM:&w=3072&h=2048&ved=0ahUKEwil0dGOl4DMAhXCqA4KHaCgCBQQMwgdKAAwAA&uact=8"]
    #start_urls = ["https://www.google.com/ncr"]
    #start_urls = ["http://content.time.com/time/covers/asia/0,16641,20140203,00.html"]
    start_urls = ["https://www.google.com/search?q=utah+homes&tbs=isz:lt%2Cislt:4mp&tbm=isch"]
    #start_urls = ["http://www.mcarthurhomes.com/assets/SiteMedia/blog_photos/IMG_0295m-01.jpg"]
    #start_urls = ["https://www.google.com/ncr"]
    #start_urls = ["https://www.google.com//images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png"]
    
    def parse3(self, response):
        img = response.css(".art-cover-photo figure a img").xpath("@src")
        imageURL = img.extract_first()
        print "hello world"
        print img
        print imageURL
        time.sleep(1)

        yield HousePicture(file_urls=["/time/images/covers/asia/2014/20140203_600.jpg"])

    def parse(self, response):
        i = 1
        driver = webdriver.Firefox()
        driver.get("https://www.google.com/search?q=utah+homes&tbs=isz:lt%2Cislt:4mp&tbm=isch")
        picture_array = [None]*40
        while i < 40:
            try:
                picture_url = driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[" +str(i) + "]/a").get_attribute("href")
                picture_url = picture_url.split('http://images.google.de/imgres?imgurl=', 1)[1]
                picture_url = picture_url.split('&imgrefurl', 1)[0]
                picture_array[i] = picture_url
                i = i + 1
            except:
                i = i + 1
                
        clean = [x for x in picture_array if x != None]

        for x in range(0, len(clean)):
            print clean[x]
            yield HousePicture(file_urls=[clean[x]])
    def parse2(self, response):
        i = 0
        while i < 1:
            driver = webdriver.Firefox()
            driver.get(start_urls)
            driver.find_element_by_xpath("/div[1]/a/img").click()
            i = 10   
        '''
        fetch 'http://scrapy.org'
        type(response)
        scrapy.http.response.html.HtmlResponse
        fetch 'http://www.scrapy.org/site-media/images/logo.png'
        type(response)
        scrapy.http.response.Response
        time.sleep(50)
        '''
        #url = response.css("img")
        #print url
        #followed_url = scrapy.Request(url.xpath("@href").extract_first())
        #print followed_url
        #img = response
        #img = response.css("img#hplogo").xpath("@src")
        #imageURL = img
        #print "hello"
        #print followed_url
        #print "hello"
        #print img
        #print imageURL
        time.sleep(5)

        yield HousePicture(file_urls=["http://www.mcarthurhomes.com/assets/SiteMedia/blog_photos/IMG_0295m-01.jpg"])
        
    def parse2(self, response):
        img = response.css("img#hplogo").xpath("@src")
        #img = response.css("img#hplogo").xpath("@src")
        imageURL = img.extract_first()
        print imageURL
        imageURL = "https://www.google.com/" + imageURL
        print imageURL
        time.sleep(5)
        yield HousePicture(file_urls=[imageURL])
        #url = response.xpath("/html/body/div/div[5]/span/center/div[1]/img").xpath("@src")
        #urlURL = url.extract_first()
        #yield HousePicture(file_urls=[urlURL])
        #pass
        #yield scrapy.Request(url.xpath("@href").extract_first(), self.parse_page)
    def parse2(self, response):
        img = response.xpath("/html/body/div/div[5]/span/center/div[1]/img").xpath("@src")
        
        imageURL = img.extract_first()
        yield HousePicture(file_urls=[imageURL])

'''
class MyHouseSpider(scrapy.Spider):
    name = "my-house-spider"
    start_urls = ["https://www.google.com/search?q=utah+homes&tbs=isz:lt%2Cislt:4mp&tbm=isch"]
    def parse(self, response):
        url = response.xpath("/html/body/div[5]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/a/img")
        yield scrapy.Request(url.xpath("@href").extract_first(), self.parse_page)
    def parse_page(self, response):
        image = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/a/img").xpath("@href")
        imageURL = img.extract_first()
        yield HousePicture(file_urls=[imageURL])
'''
