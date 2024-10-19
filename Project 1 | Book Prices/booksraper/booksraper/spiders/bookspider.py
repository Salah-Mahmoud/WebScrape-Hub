import scrapy

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'title': book.xpath('.//h3/a/@title').get(),
                'price': book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').get(),
                'instock_availability': book.xpath('.//p[contains(@class, "instock")]/text()').getall()[-1].strip(),
                'stars': book.xpath('.//p[contains(@class, "star-rating")]/@class').get().split()[-1],
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)
