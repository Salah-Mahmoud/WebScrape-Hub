import scrapy
from scrapy_selenium4 import SeleniumRequest
from scrapy.selector import Selector
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginspiderSpider(scrapy.Spider):
    name = "loginspider"

    def start_requests(self):
        url = "https://www.scrapingcourse.com/login"
        yield SeleniumRequest(
            url=url,
            callback=self.parse,
            wait_time=10,
            wait_until=EC.element_to_be_clickable((By.CSS_SELECTOR, "button#submit-button"))
        )

    def parse(self, response):
        driver = response.request.meta["driver"]
        wait = WebDriverWait(driver, timeout=10)

        driver.find_element(By.CSS_SELECTOR, "button#submit-button").click()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

        username_field = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        username_field.clear()
        username_field.send_keys("admin@example.com")

        password_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_field.clear()
        password_field.send_keys("password")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2#challenge-title")))

        selector = Selector(text=driver.page_source)

        for review in selector.css("div.product-item.flex.flex-col.items-center.rounded-lg"):
            title = review.css("span.product-name::text").get()
            price = review.css("span.product-price.text-slate-600::text").get()

            yield {
                "title": title,
                "price": price
            }
