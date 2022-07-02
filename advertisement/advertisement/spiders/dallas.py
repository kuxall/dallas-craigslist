import scrapy


class DallasSpider(scrapy.Spider):
    name = 'dallas'
    allowed_domains = ['dallas.craigslist.org']
    start_urls = [
        'https://dallas.craigslist.org/search/jjj',
    ]

    def parse(self, response):
        for jobs in response.css('div.result-info'):
            yield {
                'title': jobs.css('h3.result-heading a::text').get(),
                'url': jobs.css('h3.result-heading a::attr(href)').get(),
                'time': jobs.css('time.result-date::text').get()
            }

        # link of the next  button
        next_page = response.css('a.button.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        # pass
        # allAds = response.css("div.result-info")

        # for ad in allAds:
        # yield{
        #     'date' : response.css("time::text").get(),
        #     'link' : response.css('a.result-title::attr(href)').get(),
        #     # "link" : response.css("a::attr(href)").get(),
        # }
