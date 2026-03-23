from time import sleep

from selenium.webdriver.chrome.service import Service

import my_selenide as browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as condition

browser.driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))

browser.timeout = 5

browser.visit("https://ya.ru/")
sleep(3)

cookies_popup_accept_button = browser.element('#gdpr-popup-v3-button-all')
cookies_popup_accept_button.click()
sleep(3)

query = browser.element('[name="text"]')
query.should_be_blank()
query.set_value('yashaka selene').press_enter()
sleep(5)
