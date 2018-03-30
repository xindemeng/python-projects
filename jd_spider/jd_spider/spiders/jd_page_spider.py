# coding: UTF-8

"""
@author: xindemeng
@time: 2018/2/24 18:53
"""
import scrapy


class JDPageSpider(scrapy.Spider):

    # 爬虫的名称
    name = "jd_page_spider"

    # 允许的域名
    allowed_domains = ["jd.com"]

    start_urls = ["https://list.jd.com/list.html?cat=1315,1343,9719"]

    def parse(self, response):
        items = response.xpath("//li[@class='gl-item']")

        for item in items:
            item_name = item.xpath(".//div[@class='p-name']//em/text()").extract()[0].strip()
            item_url = item.xpath(".//div[@class='p-name']/a/@href").extract()[0]
            pic_list = item.xpath(".//div[@class='p-img']//img/@src").extract()
            if len(pic_list) > 0:
                item_pic_url = pic_list[0]
            else:
                item_pic_url = item.xpath(".//div[@class='p-img']//img/@data-lazy-img").extract()[0]
            item_data_sku = item.xpath("./div/@data-sku").extract()[0]

            print("name", item_name)
            print("url", item_url)
            print("pic_url", item_pic_url)
            print("data_sku", item_data_sku)
