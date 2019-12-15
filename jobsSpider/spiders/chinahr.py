# -*- coding: utf-8 -*-
import scrapy
import time
from jobsSpider.items import JobsspiderItem
from jobsSpider.common import printf

class ChinahrSpider(scrapy.Spider):
    name = '中华英才网'
    allowed_domains = ['www.chinahr.com']
    start_urls = ['http://www.chinahr.com/']
    positionUrl = ''
    curPage = 0
    headers = {}

    def start_requests(self):
        return [self.next_request()]

    def parse(self, response):
        print("开始请求 -> " + response.url)
        job_list = response.css('div.jobList > ul')
        if (len(job_list) > 0):
            print("中华英才网 第" +str(self.curPage)+ "页职位总数:" + str(len(job_list)))
            for job in job_list:
                item = JobsspiderItem()
                item['position_id'] = job.css('li.l1 > span.e1 > a::attr(href)').extract_first().strip().replace(
                    ".html?searchplace=22,247", "").replace("http://www.chinahr.com/job/", "")
                item["position_name"] = job.css('li.l1 > span.e1 > a::text').extract_first().strip()
                salary = job.css('li.l2 > span.e2::text').extract_first().strip().split("-")
                item["salary"] = str(int(int(salary[0]) / 1000)) + "K-" + str(int(int(salary[1]) / 1000)) + "K"
                item["avg_salary"] = (int(salary[0]) + int(salary[1])) / 2000
                info_primary = job.css('li.l2 > span.e1::text').extract_first().strip().split("/")
                item['city'] = "河南/郑州"
                item['work_year'] = info_primary[2].replace("]\r\n\t\t\t\t\t\t\t", "")
                item['education'] = info_primary[3]
                item['company_name'] = job.css('li.l1 > span.e3 > a::text').extract_first().strip()

                item['industry_field'] = ""
                item['finance_stage'] = ""
                item['company_size'] = ""

                item['position_lables'] = ""
                item['time'] = job.css('li.l1 > span.e2::text').extract_first().strip()
                item['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                item['platform'] = "chinahr"
                yield item
            yield self.next_request()

    # 发送请求
    def next_request(self):
        self.curPage += 1
        self.positionUrl = "http://www.chinahr.com/sou/?orderField=relate&keyword=c&city=312&page=" + str(
            self.curPage)
        printf("中华英才网",str(self.curPage))
        time.sleep(5)
        return scrapy.http.FormRequest(
            self.positionUrl,
            headers=self.headers,
            callback=self.parse)
