import scrapy
from imdb_top250Movies.items import ImdbTop250MoviesItem


class imdb_top250Movies(scrapy.Spider):
    name = 'imdbMovies'
    start_urls = [
        'https://www.imdb.com/chart/top/'
    ]


    def parse(self, response):
        container = response.css('td.titleColumn')
        for movies in container:
            title = movies.css('a::text').get()
            num = int(movies.css('::text').get().strip()[:3].strip().strip('.'))
            inner_site = movies.css('a::attr("href")').get()
            yield response.follow(url=inner_site, callback=self.innerSite, meta=dict(name=title, num=num))



    def innerSite(self, response):
        items = ImdbTop250MoviesItem()
        # items = dict()

        container = response.css('div[data-testid="title-pc-wide-screen"] ul.baseAlt')

        directorChild, writerChild, starsChild = container

        items['Sl_No'] = response.meta['num']
        items['Movie_Title'] = response.meta['name']
        items['Release_Year'] = response.css('ul.ipc-inline-list.ipc-inline-list--show-dividers.sc-8c396aa2-0.kqWovI.baseAlt li:first-child span::text').get()
        items['Movie_Duration'] = "".join(response.css('ul.ipc-inline-list.ipc-inline-list--show-dividers.sc-8c396aa2-0.kqWovI.baseAlt li:last-child::text').getall())
        items['IMDb_Rating'] = response.css('span.sc-7ab21ed2-1.jGRxWM::text').get() + '/10'
        items['IMDb_Customer_votes'] = response.css('div.sc-7ab21ed2-3.dPVcnq::text').get()
        items['Genre'] = response.css('div.ipc-chip-list__scroller span::text').getall()
        items['StoryLine'] = response.css("div.sc-16ede01-7.hrgVKw span:first-child::text").get()
        items['Director'] = directorChild.css('a::text').getall()
        items['Writers'] = writerChild.css('a::text').getall()
        items['Stars'] = starsChild.css('a::text').getall()
        items['Release_Date'] = response.css('li[data-testid="title-details-releasedate"] li.ipc-inline-list__item a::text').getall()
        items['Country_of_Origin'] = response.css('li[data-testid="title-details-origin"] li.ipc-inline-list__item a::text').getall()
        items['Languages'] = response.css('li[data-testid="title-details-languages"] li.ipc-inline-list__item a::text').getall()
        items['Filming_Locations'] = response.css('li[data-testid="title-details-filminglocations"] li.ipc-inline-list__item a::text').getall()
        items['Production_Companies'] = response.css('li[data-testid="title-details-companies"] li.ipc-inline-list__item a::text').getall()
        
        yield items

