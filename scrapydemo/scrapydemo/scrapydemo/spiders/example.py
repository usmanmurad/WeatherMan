import scrapy


from ..items import ScrapydemoItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/page/1/']
    page_number = 1
    def parse(self, response):
        all_div_elems = response.css('div.quote')
        item = ScrapydemoItem()
        for quote in all_div_elems:
            item['quote_text'] = quote.css('span.text::text').extract()
            item['author_name'] = quote.css('.author::text').extract()
            item['tags'] = quote.css('.tag::text').extract()
            yield item
        next_page = 'http://quotes.toscrape.com/page/' + str(QuotesSpider.page_number + 1) + '/'
        if QuotesSpider.page_number < 5:
            QuotesSpider.page_number = QuotesSpider.page_number + 1
            yield response.follow(next_page, callback=self.parse)
