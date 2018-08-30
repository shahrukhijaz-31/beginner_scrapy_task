import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class ScotlandSpider(scrapy.Spider):
    name = 'scotland'
    allowed_domains = ['www.whoownsscotland.org.uk']
    login_url = r'http://www.whoownsscotland.org.uk/login.php?p=%2Fsearch.php'
    start_urls = ['http://www.whoownsscotland.org.uk/search.php']

    def login(self , response):
        data = {
            'name' : 'USERNAME',
            'pass' : 'PASSWORD',
            'previous' : r'%2Fsearch.php',
            'login' : 'login'
        }
        yield FormRequest(url=self.login_url, formdata=data ,callback=self.parse)

    def parse(self, response):
        open_in_browser(response)
        links = response.xpath('//p/a/@href').extract()
        for link in links:
            absoulute_url = response.urljoin(link)
            yield scrapy.Request(absoulute_url , callback=self.parse_links)