from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    executable_path = {"executable_path": "C:/Users/mrjac/.wdm/drivers/chromedriver/win32/88.0.4324.96/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    listings = {}

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    listings["test"] = soup.find("a",class_ = 'test').get_text()

    browser.quit()

    return listings