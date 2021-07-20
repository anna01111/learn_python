from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from advert import ad1
import time

driver = webdriver.Chrome('./chromedriver')
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get("https://www.olx.ua/uk/")
butn = driver.find_element_by_link_text('Мій профіль')
butn.click()

time.sleep(5)

ipt1 = driver.find_element_by_id('userEmail')
ipt2 = driver.find_element_by_id('userPass')

ipt1.send_keys('annaloz11@yahoo.com')
ipt2.send_keys('Laurent1!')

butn = driver.find_element_by_id('se_userLogin')
butn.click()

# fetch data needed to recreate ads
#divs_with_ads = driver.find_elements_by_xpath("//div[@class='myoffersnew__row row-elem  ']")

divs_with_ads = driver.find_elements_by_class_name('myoffersnew__row row-elem  ')

print(divs_with_ads.text)

print(len(divs_with_ads))
for item in divs_with_ads:
    data_features = item.get_attribute('data-features')
    print(data_features)


driver.quit()


# delete ads

# recreate ads

