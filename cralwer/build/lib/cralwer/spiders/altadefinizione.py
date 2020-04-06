import scrapy




class PostsSpider(scrapy.Spider):
    name = "altadefinizione"
    page_counter = 2
    post_counter_img = 0
    post_total = 0

    start_urls = [
        "https://altadefinizione.rocks/"
    ]

    def parse(self, response):
        for post in response.css('div.wrapperImage'):
            if self.post_total < 36:
                yield {
                    'Titolo': post.css('h2.titleFilm a::text')[0].get(),
                    'Link_al_film': post.css('a::attr(href)')[0].get(),
                    'Link_immagine': post.css('img::attr(src)')[0].get(),
                }
                self.post_total = self.post_total + 1
                self.post_counter_img = self.post_counter_img + 1
            else:
                self.post_total = 0
                next_page = 'https://altadefinizione.rocks/page/' + str(self.page_counter) + '/'
                if next_page and self.page_counter != 294:
                    self.page_counter = self.page_counter + 1
                    next_page = response.urljoin(next_page)
                    yield scrapy.Request(next_page, self.parse)
