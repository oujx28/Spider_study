# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
print(driver.title)
assert u"百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys(u"网络爬虫")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"网络爬虫" in driver.page_source
driver.close()
