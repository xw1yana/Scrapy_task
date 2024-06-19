import scrapy
from rental_scraper.items import RentalItem

class HerboSpider(scrapy.Spider):
    name = "herbo"
    start_urls = ['https://bostad.herbo.se']

    def parse(self, response):
        for listing in response.css('div.property-listing'):
            item = RentalItem()
            item['url'] = response.urljoin(listing.css('a::attr(href)').get())
            item['title'] = listing.css('h2.property-title::text').get()
            item['status'] = listing.css('span.status::text').get()
            item['pictures'] = listing.css('img::attr(src)').getall()
            item['rent_price'] = listing.css('span.price::text').re_first(r'\d+')
            item['description'] = listing.css('div.description::text').get()
            item['phone_number'] = listing.css('span.phone::text').get()
            item['email'] = listing.css('span.email a::attr(href)').re_first(r'mailto:(.*)')
            yield item
