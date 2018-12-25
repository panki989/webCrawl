#!/usr/bin/env python
# coding: utf-8
'''fills the form in the site'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import ElementNotVisibleException

class Link:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)

    def fill_form(self):
        self.driver.get('https://login.live.com/')
        
        #self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'button')))
        #buttons = self.driver.find_elements_by_tag_name('input')
        #buttons = self.driver.find_elements(By.TAG_NAME,'button')
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'form')))
        forms = self.driver.find_elements(By.TAG_NAME,'form')
        
        for i in range(len(forms)):
            self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))
            inputs = forms[i].find_elements(By.TAG_NAME,'input')
            #self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'button')))
            buttons = forms[i].find_elements(By.TAG_NAME,'button')
            for j in range(len(inputs)):
                try:
                    val_type = inputs[j].get_attribute('type')
                except:
                    print("Some input doesn't have type value!!!")
                if val_type.strip() == 'text':
                    try:
                        inputs[j].send_keys("random txt")
                    except:
                        print("Hidden text field!!!")
                elif val_type.strip() == 'email':
                    try:
                        inputs[j].send_keys("random mail")
                    except:
                        print("Hidden text field!!!")
                elif val_type.strip() == 'password':
                    try:
                        inputs[j].send_keys("random pwd")
                    except:
                        print("Hidden password Field!!!")
                elif val_type.strip() == 'radio':
                    inupts[j].click()
                elif val_type.strip() == 'submit':
                    inputs[j].send_keys(Keys.CONTROL + Keys.ENTER)
                else:
                    for k in range(len(buttons)):
                        bt_type = buttons[k].get_attribute('type')
                        if bt_type.strip() == 'submit':
                            buttons[k].send_keys(Keys.CONTROL + Keys.ENTER)




    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    obj = Link()
    obj.fill_form()
    #obj.quit()
