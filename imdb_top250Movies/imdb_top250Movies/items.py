# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbTop250MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Sl_No = scrapy.Field()
    Movie_Title = scrapy.Field()
    Release_Year = scrapy.Field()
    Movie_Duration = scrapy.Field()
    IMDb_Rating = scrapy.Field()
    IMDb_Customer_votes = scrapy.Field()
    Genre = scrapy.Field()
    StoryLine = scrapy.Field()
    Director = scrapy.Field()
    Writers = scrapy.Field()
    Stars = scrapy.Field()
    Release_Date = scrapy.Field()
    Country_of_Origin = scrapy.Field()
    Languages = scrapy.Field()
    Filming_Locations = scrapy.Field()
    Production_Companies = scrapy.Field()