import scrapy


class DallasSpider(scrapy.Spider):
    name = 'titles'
    allowed_domains = ['https://dallas.craigslist.org/search/jjj']
    start_urls = ['http://dallas.craigslist.org/search/jjj/']

    def parse(self, response):
       job = {}
       job['url'] = response.css('a.result-title::attr(href)').get()
       return job
        # yield{
        #     'link': response.xpath("//a/@href").extract(),
        #     'posted-date': response.xpath('//*[@id="search-results"]/li[1]/div/time/text()').getall(),
        # }
