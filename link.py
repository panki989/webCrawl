#!/usr/bin/env python
# coding: utf-8
'''return links & buttons of site'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Link:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)

    def get_links(self):
        print('--------Links-------------')
        self.driver.get('https://login.yahoo.com')
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
        links = self.driver.find_elements_by_tag_name('a')
        for x in range(len(links)):
            print(links[x].text, " : ", links[x].get_attribute('href'))
        print('______________________________________________\n')
        self.get_buttons(self.driver)
        

    def get_buttons(self,driver):
        print('--------Buttons-------------')
        buttons = driver.find_elements_by_tag_name('input')
        for y in range(len(buttons)):
            print(buttons[y].get_attribute('type'), " : ", buttons[y].get_attribute('value'))

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    obj = Link()
    try:
        obj.get_links()
    finally:
        obj.quit()
