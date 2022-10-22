import scrapy

class Merli(scrapy.Spider):
    name = 'riviera'
    start_urls = ['http://rivieramaya.org.mx/hoteles/']
    custom_settings = {
        'FEED_URI': 'riviera.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'ROBOTSTXT_OBEY': True,
    }

    LINK_POST = '//h2[@class = "entry-title"]/a/@href'
    NEW_PAGE_BOTTON = '//div[@class = "wp-pagenavi"]/a[@class = "nextpostslink"]/@href'


    def parse(self, response):
        links_post = response.xpath(self.LINK_POST).getall()
        yield {'links': links_post}

        next_page_button_link = response.xpath(self.NEW_PAGE_BOTTON).get()

        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)



