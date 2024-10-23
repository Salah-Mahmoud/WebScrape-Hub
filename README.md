# Web Scraping Projects

This repository contains various web scraping projects utilizing **Scrapy** and **Selenium**, each designed to scrape data from different types of websites and overcome common web scraping challenges.

## Overview of Projects

### 1. **Book Price Scraper**
- **Description**: Extracts book titles and prices from the website [Books to Scrape](http://books.toscrape.com/).
- **Technologies**: Scrapy.

### 2. **Login-Protected Pages Scraper**
- **Description**: Scrapes content from login-protected pages on [Scraping Course Login](https://www.scrapingcourse.com/login) by automating the login process using Selenium.
- **Technologies**: Scrapy, Selenium, WebDriver Manager.

### 3. **Infinite Scrolling Scraper**
- **Description**: Extracts data from pages with infinite scrolling functionality on [Scraping Course Scroll](https://www.scrapingcourse.com/infinite-scrolling) using Selenium to handle automated scrolling.
- **Technologies**: Scrapy, Selenium.

### 4. **JavaScript-Rendered Content Scraper**
- **Description**: Scrapes dynamically-rendered content from JavaScript-heavy pages on [Scraping Course Rendering](https://www.scrapingcourse.com/javascript-rendering) using Selenium for proper rendering.
- **Technologies**: Scrapy, Selenium.


## Requirements

To run any project, make sure you have the following installed:
- Python 
- Scrapy
- Selenium (for projects requiring Selenium)
- `webdriver-manager` (for Selenium management)


### Note for Selenium Projects
If the project uses Selenium, you will need to install a web browser driver (e.g., ChromeDriver or GeckoDriver):
- Install `ChromeDriver` for Google Chrome.
- Install `GeckoDriver` for Mozilla Firefox.

