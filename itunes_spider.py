from scrapy import Spider

class Itunes_Spider(Spider):
    name='apple'
    start_urls=['https://www.apple.com/in/itunes/charts/songs/']
    
    def parse(self,response):
        area=response.css("div.section-content")
        for item in area.css('li'):
            yield{
                "rank":item.css("strong::text").extract_first(),
                "title":item.css("h3 a::text").extract_first(),
                "artist":item.css("h4 a::text").extract_first(),
            }
        