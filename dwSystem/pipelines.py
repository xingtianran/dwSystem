# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class DwsystemPipeline(object):
    def process_item(self, item, spider):
        with open('data/data.csv', 'a', newline='', encoding="utf-8") as f:
            myWriter = csv.writer(f)
            myWriter.writerow([item["title"], item["summary"].replace(" ", "").replace("\n", "").replace("\t", ""), item["address"]])
            f.close()
