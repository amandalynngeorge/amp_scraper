import scrapy

class AmpScraperItem(scrapy.Item):
    url_from = scrapy.Field()
    url_to = scrapy.Field()
pass
