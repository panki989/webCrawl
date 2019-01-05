#!/usr/bin/env python
# coding: utf-8
'''fills the form in the site'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

class Link:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)

    def fill_form(self):
        self.driver.get('https://outlook.live.com/owa/')
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
        self.driver.find_element(By.LINK_TEXT,'Sign in').click()

        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))
        inputs = self.driver.find_elements(By.TAG_NAME,'input')
        for j in range(len(inputs)):
            try:
                val_type = inputs[j].get_attribute('type')
            except:
                print("Some input doesn't have type value!!!")

            if val_type.strip() == 'email':
                try:
                    mail = "yourmail@gmail.com"
                    inputs[j].send_keys(mail)
                    inputs[j].send_keys(Keys.ENTER)
                    break
                except:
                    print("Hidden text field!!!")

        pwd = 'YourPwd'
        val = True
        while (val == True):
            try:
                self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))
                input1 = self.driver.find_element(By.NAME,'passwd')
                input1.clear()
                input1.send_keys(pwd)
                self.wait.until(EC.text_to_be_present_in_element_value((By.NAME, 'passwd'), pwd), 5)
                input2 = self.driver.find_element(By.ID,'idSIButton9')    
                input2.submit()
                val = False
            except TimeoutException:
                val = True
                
        input3 = self.driver.find_element(By.TAG_NAME,'button')
        input3.click()

        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'_2cXU4NRwaysHkyJPwe9DZP')))
        link_data = self.driver.find_element(By.CLASS_NAME,'_2cXU4NRwaysHkyJPwe9DZP')
        links = link_data.find_elements(By.TAG_NAME, 'a')
        for i in range(len(links)):
            print(links[i].text, " : ", links[i].get_attribute('href'))

    def quit(self):
        time.sleep(10)
        self.driver.quit()

if __name__ == '__main__':
    obj = Link()
    obj.fill_form()
    obj.quit()
