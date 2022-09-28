import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = [
        'https://www.goodreads.com/author/quotes/2056.Thomas_Sowell',

    ]

    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'author': quote.xpath('span/small/text()').get(),
    #             'text': quote.css('span.text::text').get(),
    #         }

    #     next_page = response.css('li.next a::attr("href")').get()
    #     if next_page is not None:
    #         yield response.follow(next_page, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):

            print(quote.xpath('span/text()').get())

    


#scrapy runspider gdscraper.py -o tsquotes.jl

