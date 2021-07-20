from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.expected_conditions import *
from time import sleep

"""
https://selenium-python.readthedocs.io/

https://www.selenium.dev/selenium/docs/api/py/api.html
"""

with webdriver.Chrome() as browser:
    browser.get("https://techstepacademy.com/training-ground")

    butn1 = browser.find_element_by_id("b1")
    butn1.click()

    WebDriverWait(browser, 5).until(alert_is_present())

    alert = Alert(browser)
    print(alert.text)

    assert alert.text == 'You clickedButton1.'
    alert.accept()

    dropdown = browser.find_element_by_id('sel1')
    my_dropdown = Select(dropdown)

    dropdown_info = [item.text for item in my_dropdown.options]
    print(dropdown_info)

    my_dropdown.select_by_index(1)  # 'Beets'

    print(my_dropdown.first_selected_option.text)
    assert my_dropdown.first_selected_option.text == 'Beets'
