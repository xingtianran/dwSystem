from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.dw_spider import DwSpiderSpider


if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(DwSpiderSpider)
    process.start()
