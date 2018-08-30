import scrapy


class UMTSpider(scrapy.Spider):
    name = "umt_scraper"
    start_urls = [
        'https://www.umt.edu.pk/',
    ]

    def parse(self, response):
            for link in response.css("ul.nav li a::attr(href)"):
                yield response.follow(link, self.parse_code)

   :
