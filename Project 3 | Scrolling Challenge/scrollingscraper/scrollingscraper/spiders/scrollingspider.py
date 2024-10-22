import scrapy
from scrapy_selenium4 import SeleniumRequest
from scrapy.selector import Selector
import time

class ScrollingspiderSpider(scrapy.Spider):
    name = "scrollingspider"

    def start_requests(self):
        url = "https://www.scrapingcourse.com/infinite-scrolling"
        yield SeleniumRequest(
            url=url,
            callback=self.parse,
            wait_time=10,
        )

    def parse(self, response):
        driver = response.request.meta["driver"]
        # Get the initial scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(2)

            # Get the new scroll height after scrolling
            new_height = driver.execute_script("return document.body.scrollHeight")

            # Break the loop if we've reached the bottom of the page
            if new_height == last_height:
                break

            last_height = new_height

        selector = Selector(text=driver.page_source)

        for review in selector.css("div.product-item.flex.flex-col.items-center.rounded-lg"):
            title = review.css("span.product-name::text").get()
            price = review.css("span.product-price.text-slate-600::text").get()

            yield {
                "title": title,
                "price": price
            }
