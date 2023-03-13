import scrapy

from scrapy_tutorial.items import PortfolioItem


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["scm-mm.com"]
    start_urls = ['https://scm-mm.com/en/portfolio/']

    def parse(self, response):
        for data in response.css('div.portfolio-content ul.contents li'):
            item = PortfolioItem()

            item['title'] = data.css('div.port-txt p.port-tit::text').get()
            item['details_link'] = data.css('a::attr(href)').get()
            item['image'] = data.css('div.port-img img::attr(src)').get()

            yield item

