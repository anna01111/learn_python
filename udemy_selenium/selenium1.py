from selenium import webdriver


"""
https://selenium-python.readthedocs.io/locating-elements.html
"""


browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")


# Assign elements
input2_elem = browser.find_element_by_id('ipt1')
butn4_elem = browser.find_element_by_xpath("//button[@id='b4']")

# Manipulate elements
input2_elem.send_keys("Test text")
butn4_elem.click()


