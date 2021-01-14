from selenium import webdriver


def scrape():
    """
    Scrapes property portal
    """
    browser = webdriver.Chrome()
    browser.get('http://seleniumhq.org/')
