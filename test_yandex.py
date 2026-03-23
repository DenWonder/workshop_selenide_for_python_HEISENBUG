from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import selenide as browser
browser.driver = webdriver.Chrome(ChromeDriverManager().install())

browser.visit("https://ya.ru/")
sleep(3)

browser.driver.find_element(By.CSS_SELECTOR, "#gdpr-popup-v3-button-all").click()
sleep(3)


browser.Element('[name="text"]').should_be_blank()

browser.driver.find_element(By.NAME, "text").click()
browser.driver.find_element(By.NAME, "text").send_keys("Selene" + Keys.ENTER)

sleep(5)



