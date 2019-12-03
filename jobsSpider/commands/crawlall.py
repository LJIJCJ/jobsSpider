# -*- coding: utf-8 -*-
# @Author: Mardan
# @Date:   2019-12-03 10:32:17
# @Last Modified by:   Mardan
# @Last Modified time: 2019-12-03 10:43:48

from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        spider_list = self.crawler_process.spiders.list()
        for name in spider_list:
            print("********** 启动爬虫:"+name+"-------->")
            self.crawler_process.crawl(name, **opts.__dict__)
        self.crawler_process.start()
