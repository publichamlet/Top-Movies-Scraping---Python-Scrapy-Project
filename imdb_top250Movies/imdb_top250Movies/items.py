# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbTop250MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    duration = scrapy.Field()
    rating = scrapy.Field()
    total_votes = scrapy.Field()
    genre = scrapy.Field()
    storyLine = scrapy.Field()
    director = scrapy.Field()
    writers = scrapy.Field()
    stars = scrapy.Field()
    pass
