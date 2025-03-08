import scrapy
from dwSystem.items import DwsystemItem
import csv
import time


class DwSpiderSpider(scrapy.Spider):
    name = "dw_spider"
    allowed_domains = ["www.gitee.com"]
    url = "http://www.gitee.com/explore/all"
    target_url = "http://www.gitee.com"

    currentPage = 1

    def __init__(self):
        with open('data.csv', 'a', newline='', encoding="utf-8") as f:
            myWriter = csv.writer(f)
            myWriter.writerow(['仓库名称', '仓库概述', '仓库地址'])
            f.close()

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        lis = response.xpath("//div[@class='ui relaxed divided items explore-repo__list']/div")
        for each in lis:
            item = DwsystemItem()
            item['title'] = each.xpath("div/div[1]/div[1]/h3/a/text()").extract()[0]
            detail_href_suffix = each .xpath("div/div[1]/div[1]/h3/a/@href").extract()[0]
            detail_href = self.target_url + detail_href_suffix
            yield scrapy.Request(detail_href, callback=self.parse_detail, meta={"item": item})
        if self.currentPage < 100:
            time.sleep(5)
            self.currentPage += 1
            yield scrapy.Request("http://www.gitee.com/explore/all?page=" + str(self.currentPage),
                                 callback=self.parse)

    def parse_detail(self, response):
        item = response.meta["item"]
        item['summary'] = response.xpath("//div[@id='project-wrapper']/div[2]/div/div[1]/div[2]/span/text()").extract()[0]
        item['address'] = response.xpath("//div[@id='git-project-download-panel']/div[2]/div[1]/a[1]/@data-url").extract()[0]
        yield item
