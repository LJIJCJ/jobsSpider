# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position_id = scrapy.Field()
    position_name = scrapy.Field()
    position_lables = scrapy.Field()
    work_year = scrapy.Field()
    salary = scrapy.Field()
    avg_salary = scrapy.Field()
    city = scrapy.Field()
    education = scrapy.Field()
    company_name = scrapy.Field()
    industry_field = scrapy.Field()
    finance_stage = scrapy.Field()
    company_size = scrapy.Field()
    time = scrapy.Field()
    updated_at = scrapy.Field()
    platform = scrapy.Field()
