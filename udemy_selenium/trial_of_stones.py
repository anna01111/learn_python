from selenium import webdriver

"""
https://selenium-python.readthedocs.io/

https://www.selenium.dev/selenium/docs/api/py/api.html
"""


browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")

# first riddle
# Assign elements
inpt1_elem = browser.find_element_by_id('r1Input')
butn1_elem = browser.find_element_by_id('r1Btn')


# Manipulate elements
inpt1_elem.send_keys("rock")
butn1_elem.click()

# Get password
#psswd = browser.find_element_by_xpath("//div[@id='passwordBanner']/h4").text
passwd = browser.find_element_by_css_selector("div#passwordBanner > h4").text

print(passwd)

# second riddle
# Assign elements
inpt2_elem = browser.find_element_by_id('r2Input')
butn2_elem = browser.find_element_by_id('r2Butn')

# Manipulate elements
inpt2_elem.send_keys(passwd)
butn2_elem.click()


# third riddle
richest_merchant_name = browser.find_element_by_xpath("//p[text()='3000'] /.. /span").text

# Assign elements
inpt3_elem = browser.find_element_by_id('r3Input')
butn3_elem = browser.find_element_by_id('r3Butn')

# Manipulate elements
inpt3_elem.send_keys(richest_merchant_name)
butn3_elem.click()

complete_msg = browser.find_element_by_css_selector("div#trialCompleteBanner h4").text
print(complete_msg)

#assert complete_msg == "Trial Complete"


browser.quit()

