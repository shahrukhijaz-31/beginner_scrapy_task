import scrapy


class QuotesSpider(scrapy.Spider):
    name = "webScrap"
    start_urls = [
        'https://www.sheego.de/damenschuhe-adidas/',
    ]
    def parse(self, response):
        for link in response.css('img.cj-product__image'):
            yield {
                'imgLink' : link.css('img.cj-product__image::attr(title)'),
            }