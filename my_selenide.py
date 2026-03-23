from __future__ import annotations

from typing import Callable


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

from wait import WebDriverWait

driver: WebDriver = ...
timeout: int = 5

def wait():
    return WebDriverWait(driver, timeout=timeout,
                         ignored_exceptions=(WebDriverException,))

class element_value_is_empty(object):
    def __init__(self, locate: Callable[[], WebElement]):
        self.locate = locate

    def __call__(self, driver):
        return self.locate().get_attribute("value") == ''

    def __str__(self):
        return f"value of element {self.locate} is empty"


class Element:
    def __init__(self, locate: Callable[[], WebElement]):
        self.locate = locate

    def should_be_blank(self):
        wait().until(element_value_is_empty(self.locate))
        return self

    def set_value(self, text) -> Element:
        def command(driver):
            webelement = self.locate()
            webelement.clear()
            webelement.send_keys(text)
            return True
        wait().until(command)
        return self

    def press_enter(self) -> Element:
        self.locate().send_keys(Keys.ENTER)
        return self

    def click(self) -> Element:
        self.locate().click()
        return self

    def element(self, selector: str) -> Element:
        def locate():
            original = self.locate()
            try:
                webelement = original.find_element(By.CSS_SELECTOR, selector)
                return webelement
            except Exception as error:
                outer_html = original.get_attribute('outerHTML')
                raise WebDriverException(
                    msg=f'failed to find inside {outer_html} '
                        f'the element by: {selector}'
                )

        return Element(locate)


def visit(url):
    driver.get(url)


def element(selector: str):
    return Element(lambda: driver.find_element(By.CSS_SELECTOR, selector))