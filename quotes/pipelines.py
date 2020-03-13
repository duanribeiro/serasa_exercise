# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class ProjectPipeline(object):

    def __init__ (self):
        self.conn = pymongo.MongoClient(
           "mongodb+srv://duanribeiro:BJ183r32@futebol-iwbwh.mongodb.net/test?retryWrites=true&w=majority",
            27017
        )

        # Utilizar o banco de dados dentro do servidor
        db = self.conn['test']
        self.collection = db['quotes']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))

        return item