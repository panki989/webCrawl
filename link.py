#!/usr/bin/env python
# coding: utf-8
'''return links & buttons of site'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
import time
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import re
import logging

class Link:
    def __init__(self):

        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)
    
    def initDriver(self,url):
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 5)
        self.performInput()
        self.performButton()
        self.performerLink()
        
    def performButton(self):

        rawbuttons = self.get_buttons()            #Get (class, id) for buttons

    def get_buttons(self):

        print('--------Buttons-------------')
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'button')))
        buttons = self.driver.find_elements(By.TAG_NAME, 'button')
        rawbuttons = []
        for x in range(len(buttons)):
            print(buttons[x].get_attribute('class'), " : ", buttons[x].get_attribute('id'))
            rawbuttons.append((buttons[x].get_attribute('class'),buttons[x].get_attribute('id')))
        print("Total buttons ", len(buttons))
        print('______________________________________________\n')
        return rawbuttons
    
    def performerLink(self):

        rawlinks = self.get_links()
        for i in range(len(rawlinks)):
            self.driver.execute_script("window.open('');")
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])
            try:
                self.driver.get(rawlinks[i])
            except InvalidArgumentException:
                print("Invalid type url is catched!!!")
            time.sleep(3)
            self.driver.close()
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[0])

    def get_links(self):

        print('--------Links-------------')
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        rawlink = []
        for x in range(len(links)):
            print(links[x].text, " : ", links[x].get_attribute('href'))
            rawlink.append(links[x].get_attribute('href'))
        print("Total links ", len(links))
        print('______________________________________________\n')
        return rawlink

    def performInput(self):

        inputs = self.get_inputs()   #list of [(type, name, id)]
        print(inputs)
        for field in inputs:
            if field[0] == 'text':
                try:
                    self.driver.find_element(By.ID, field[2]).send_keys("text11")
                except NoSuchElementException:
                    self.driver.find_element(By.NAME, field[1]).send_keys("text12")
                except ElementNotVisibleException:
                    print("Hidden text input by CSS!!!")
                except ElementNotInteractableException:
                    print("Element is not reachble as of now!!!")
            elif field[0] == 'email':
                try:
                    self.driver.find_element(By.ID, field[2]).send_keys("abc@mail.com")
                except ElementNotVisibleException:
                    print("Hidden mail input by CSS!!!")    
            elif field[0] == 'password':
                try:
                    self.driver.find_element(By.ID, field[2]).send_keys("MyPa55w@rd")
                except ElementNotVisibleException:
                    print("Hidden password input by CSS!!!")
            elif field[0] == 'radio':
                try:
                    self.driver.find_element(By.ID, field[2]).click()
                except NoSuchElementException:
                    print("ID field is blank!!")
                except ElementNotVisibleException:
                    print("Radio button is hidden!!!")
            elif field[0] == 'submit':
                # self.driver.find_element(By.ID, field[2]).click()
                print("See you again!!!")
            else:
                print("Need to catch the type ",field[0])
        print('______________________________________________\n')

    def get_inputs(self):

        print('--------Inputs-------------')
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))
        inputs = self.driver.find_elements(By.TAG_NAME, 'input')
        input_details = []
        for y in range(len(inputs)):
            # print(inputs[y].get_attribute('type'), " : ",  inputs[y].get_attribute('value'),
                # " : ", inputs[y].get_attribute('id'))
            if inputs[y].get_attribute('type').strip() != 'hidden':
                input_details.append((inputs[y].get_attribute('type'),inputs[y].get_attribute('name'),
                 inputs[y].get_attribute('id')))

        print("Total fields ", len(input_details))
        return input_details

    def Quit(self):
        self.driver.quit()

if __name__ == '__main__':
    
    def checkURL(url):
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

    if len(sys.argv) == 1:
        print("Enter the site to crawl:(Without https/http)")
        str = input()
    else:
        str = sys.argv[1]
        
    url = "https://"+str
    if checkURL(url):
        obj = Link()
        try:
            obj.initDriver(url)
        finally:
            obj.Quit()        
    else:
        print("Invalid URL given!!!")
    
