# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

from python.items import ListingItem



class PythonPipeline(object):
    item=ListingItem()
    
    def __init__(self):
            try:
                self.conn= pymysql.connect(user='ash', passwd='!@#$', host='127.0.0.1', db='javalist', use_unicode=True, charset='utf8')
                print("connected success")
                self.cursor = self.conn.cursor()
                self.cursor.execute("CREATE TABLE IF NOT EXISTS python(project_name VARCHAR(200), urls VARCHAR(200)) ")
                self.conn.commit()
            except (AttributeError, pymysql.OperationalError) as e:
                 raise e
   
    def __getitem__(self, item):
        return self.item.get('project_name')
        return self.item.get('urls')
    
    def process_item(self, item, spider): 
            #item=ListingItem()
            try:
                self.conn.cursor().execute("INSERT INTO python(project_name,urls,language_id)VALUES( %s, %s,%s)",(item['project_name'],item['urls'],2))

                                    
                self.conn.commit()
                
            except pymysql.Error as e:
                print ("Error %d: %s" % (e.args[0], e.args[1]))
                print("Not success")
                #return item.get('project_name')
                #return item.get('urls')
                return item
