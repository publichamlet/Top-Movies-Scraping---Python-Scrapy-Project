import os, sys
import scrapy
from time import perf_counter

if sys.platform.startswith('linux'):
    os.chdir(('/'.join(os.path.dirname(__file__).split('/')[:-2])))

start = perf_counter()

class imdb_top250Movies(scrapy.Spider):
    name = 'imdbMovies'
    start_urls = [
        'https://www.imdb.com/chart/top/'
    ]


    def parse(self, response):
        container = response.css('td.titleColumn')
        for movies in container:
            title = movies.css('a::text').get()
            num = movies.css('::text').get().strip()[:3]
            inner_site = movies.css('a::attr("href")').get()
            yield response.follow(url=inner_site, callback=self.innerSite, meta=dict(name=title, num=num))



    def innerSite(self, response):
        # items = ImdbTop250MoviesItem()
        items = dict()

        container = response.css('div[data-testid="title-pc-wide-screen"] ul.baseAlt')

        directorChild, writerChild, starsChild = container

        items['Sl No:'] = response.meta['num']
        items['Movie Title'] = response.meta['name']
        items['Release Year'] = response.css('ul.ipc-inline-list.ipc-inline-list--show-dividers.sc-8c396aa2-0.kqWovI.baseAlt li:first-child span::text').get()
        items['Movie Duration'] = "".join(response.css('ul.ipc-inline-list.ipc-inline-list--show-dividers.sc-8c396aa2-0.kqWovI.baseAlt li:last-child::text').getall())
        items['IMDb Rating'] = response.css('span.sc-7ab21ed2-1.jGRxWM::text').get() + '/10'
        items['IMDb Customer_votes'] = response.css('div.sc-7ab21ed2-3.dPVcnq::text').get()
        items['Genre'] = response.css('div.ipc-chip-list__scroller span::text').getall()
        items['StoryLine'] = response.css("div.sc-16ede01-7.hrgVKw span:first-child::text").get()
        items['Director'] = directorChild.css('a::text').getall()
        items['Writers'] = writerChild.css('a::text').getall()
        items['Stars'] = starsChild.css('a::text').getall()
        items['Release Date'] = response.css('li[data-testid="title-details-releasedate"] li.ipc-inline-list__item a::text').getall()
        items['Country of Origin'] = response.css('li[data-testid="title-details-origin"] li.ipc-inline-list__item a::text').getall()
        items['Languages'] = response.css('li[data-testid="title-details-languages"] li.ipc-inline-list__item a::text').getall()
        items['Filming Locations'] = response.css('li[data-testid="title-details-filminglocations"] li.ipc-inline-list__item a::text').getall()
        items['Production Companies'] = response.css('li[data-testid="title-details-companies"] li.ipc-inline-list__item a::text').getall()
        
        yield items


os.system('scrapy crawl imdbMovies -O MovieList-Generated.csv')
print(perf_counter() - start)
