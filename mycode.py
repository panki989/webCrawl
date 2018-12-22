#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.wappalyzer.com")
inputElement = driver.find_element_by_name("hostname")

#input your site here:
inputElement.send_keys("paytm.com")
inputElement.send_keys(Keys.ENTER)

try:
    data = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/section[3]/div/div/div[1]/p[1]/a[1]")))
    data1 = driver.find_elements_by_xpath("/html/body/section[3]/div/div/div[1]/p[1]")
    print(data1[0].text)
finally:
    driver.quit()