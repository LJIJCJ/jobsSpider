# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
from twisted.enterprise import adbapi


class JobsspiderPipeline(object):
    @classmethod
    def from_settings(cls, settings):
#        dbparams = dict(
#            host=settings['MYSQL_HOST'],
#            db=settings['MYSQL_DBNAME'],
#            user=settings['MYSQL_USER'],
#            passwd=settings['MYSQL_PASSWD'],
#            charset='utf8',
#            cursorclass=pymysql.cursors.DictCursor,
#            use_unicode=False,
#        )


        dbpool = adbapi.ConnectionPool('sqlite3', 'jobs', check_same_thread=False)
        return cls(dbpool)

    def __init__(self, dbpool):
        self.dbpool = dbpool

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self._handle_error, item, spider)
        return item

    def _conditional_insert(self, tx, item):
        # print item['name']
        position_id = (item["position_id"], item["platform"])
        sql = "select * from jobs where position_id='%s' and platform='%s'"%position_id
        result = tx.execute(sql)
        
        if (result != 0):
            params = (
                item["position_id"], item["position_name"], item["position_lables"], item["work_year"], item["salary"],
                item["city"], item["education"], item["company_name"], item["industry_field"],
                item["finance_stage"], item["company_size"], item["updated_at"], item["time"],
                item["platform"], item["avg_salary"])
            sql = "insert into jobs(position_id,position_name,position_lables,work_year,salary,city,education,company_name,industry_field,finance_stage,company_size,updated_at,time,platform,avg_salary) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%params
            print(sql)
            tx.execute(sql)

    def _handle_error(self, failue, item, spider):
        print(  item["position_id"], item["position_name"], item["position_lables"], item["work_year"], item["salary"],
                item["city"], item["education"], item["company_name"], item["industry_field"],
                item["finance_stage"], item["company_size"], item["updated_at"], item["time"],
                item["platform"], item["avg_salary"])
        print(failue)
