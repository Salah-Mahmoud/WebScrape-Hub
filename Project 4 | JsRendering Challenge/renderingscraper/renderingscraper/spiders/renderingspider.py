import scrapy
from scrapy_selenium4 import SeleniumRequest
from scrapy.selector import Selector


class RenderingspiderSpider(scrapy.Spider):
    name = "renderingspider"

    def start_requests(self):
        url = "https://www.scrapingcourse.com/javascript-rendering"
        yield SeleniumRequest(
            url=url,
            callback=self.parse,
            wait_time=10,
        )

    def parse(self, response):
        driver = response.request.meta["driver"]

        selector = Selector(text=driver.page_source)

        for review in selector.css("div.product-item.flex.flex-col.items-center.rounded-lg"):
            title = review.css("span.product-name::text").get()
            price = review.css("span.product-price.text-slate-600::text").get()

            yield {
                "title": title,
                "price": price
            }
