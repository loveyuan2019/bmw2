# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem

class BmwSpiderSpider(scrapy.Spider):
    name = 'bmw_spider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        uiboxes=response.xpath(r"//div[@class='uibox']")[1:]
        for uibox in uiboxes:
            category=uibox.xpath(r".//div[@class='uibox-title']/a/text()").get()
            # print(category)
            urls=uibox.xpath(r".//ul/li/a/img/@src").getall()
            # print(urls)
            urls=list(map(lambda url: response.urljoin(url),urls))
            # print(urls)
            item=BmwItem(category=category,image_urls=urls)
            yield item
        # pass
