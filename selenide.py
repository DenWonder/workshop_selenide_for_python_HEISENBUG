from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')
chrome_options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
# driver = webdriver.Chrome(options=chrome_options)
driver: WebDriver = ...
def wait():
    return WebDriverWait(driver, timeout=5)

class element_value_is_empty(object):
    def __init__(self, selector):
        self.selector = selector

    def __call__(self, driver):
        return driver.find_element(By.CSS_SELECTOR, self.selector).get_attribute("value") == ''

    def __str__(self):
        return f"value of element {self.selector} is empty"


class Element:
    def __init__(self, selector):
        self.selector = selector

    def should_be_blank(self):
        wait().until(element_value_is_empty(self.selector))


def visit(url):
    driver.get(url)