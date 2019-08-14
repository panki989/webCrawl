#!/usr/bin/env python
# coding: utf-8
'''return links & buttons of site'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
# from selenium.common.exceptions import InvalidArgumentException
import re
import sys
import time

class Link:
    
    def __init__(self):

        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)
    
    
    def initDriver(self,url):
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 5)
        try:
            error = self.driver.find_element(By.CLASS_NAME, 'error-code')
            print(error.text)
        except NoSuchElementException:
            testURL = Validation()
            message = self.driver.title
            print(message)
            if testURL.checkTEXT(message):
                print("Invalid Web page/ Page not found error!!!")
            else:
                print("Valid web page!!!")
                self.performInput()
                self.performButton()
                self.performerLink()
        
    
    def performButton(self):

        rawbuttons = self.get_buttons()              #Get (id, name, class) for buttons
        prev_url = self.driver.current_url
        for field in rawbuttons:
            print(field)
            try:
                self.driver.find_element(By.ID, field[0]).click()
            except ElementNotVisibleException:
                print("Hidden buttons in page!!!")
            except NoSuchElementException:
                try:
                    self.driver.find_element(By.NAME, field[1]).click()
                except ElementNotVisibleException:
                    print("Element is hidden!!!")
                except NoSuchElementException:
                    try:
                        self.driver.find_element(By.CLASS_NAME, field[2]).click()
                    except InvalidSelectorException:
                        print("Multiple class arguments are given....")
                    except NoSuchElementException:
                        print("All fields are blank!!!!")
                    except ElementNotVisibleException:
                        print("Element is HIDDEN!!!")
                    except WebDriverException:
                        print("Element present but not clickable!!!")

            curr_url = self.driver.current_url
            time.sleep(5)
            if prev_url != curr_url:
                print("Page changed......")
                time.sleep(4)
                self.driver.get(prev_url)
                self.performInput()
            else:
                print("alert & other links need to be catched!!!")
        print('______________________________________________\n')


    def get_buttons(self):

        print('--------Buttons-------------')
        try:
            self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'button')))
            self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))
        except TimeoutException:
            pass
        buttons = self.driver.find_elements(By.TAG_NAME, 'button')
        submit_input = self.driver.find_elements(By.TAG_NAME, 'input')
        rawbuttons = []
        for x in range(len(buttons)):
            print(buttons[x].get_attribute('id'), " : ", buttons[x].get_attribute('name'),
                " : ", buttons[x].get_attribute('class'))
            rawbuttons.append((buttons[x].get_attribute('id'),buttons[x].get_attribute('name'),
                buttons[x].get_attribute('class')))
        
        for x in range(len(submit_input)):
            if submit_input[x].get_attribute('type').strip() == 'submit':
                print(submit_input[x].get_attribute('id'), " : ", submit_input[x].get_attribute('name'),
                    " : ", submit_input[x].get_attribute('class'))
                rawbuttons.append((submit_input[x].get_attribute('id'),submit_input[x].get_attribute('name'),
                    submit_input[x].get_attribute('class')))

        print("Total buttons ", len(rawbuttons))
        return rawbuttons
    
    
    def performerLink(self):

        rawlinks = self.get_links()
        testURL = Validation()
        for i in range(len(rawlinks)):
            if testURL.checkURL("%s" % (rawlinks[i])):  
                self.driver.execute_script("window.open('');")
                time.sleep(3)
                self.driver.switch_to.window(self.driver.window_handles[1])
                
                self.driver.get(rawlinks[i])
                try:
                    error = self.driver.find_element(By.CLASS_NAME, 'error-code')
                    print(error.text)
                except NoSuchElementException:
                    message = self.driver.title
                    if testURL.checkTEXT(message):
                        print("Invalid Web page/ Page not found error!!!")
                    else:
                        print("Valid web page!!!")
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
                    try:
                        self.driver.find_element(By.NAME, field[1]).send_keys("text12")
                    except ElementNotInteractableException:
                        print("Element is not reachble as of NOW!!!")
                    except NoSuchElementException:
                        print("All fields are blank,It seems!!!")
                    except ElementNotVisibleException:
                        print("Input is hidden!!!")
                except ElementNotVisibleException:
                    print("Hidden text input by CSS!!!")
                except ElementNotInteractableException:
                    print("Element is not reachble as of now!!!")
            elif field[0] == 'email':
                try:
                    self.driver.find_element(By.ID, field[2]).send_keys("abc@mail.com")
                except ElementNotInteractableException:
                    print("Input field is there but not intractable due to javascript!!!")
                except ElementNotVisibleException:
                    print("Hidden mail input by CSS!!!")   
            elif field[0] == 'password':
                try:
                    self.driver.find_element(By.ID, field[2]).send_keys("MyPa55w@rd")
                except NoSuchElementException:
                    try:
                       self.driver.find_element(By.NAME, field[1]).send_keys("MyPa55w@rd")
                    except ElementNotInteractableException:
                        print("Password filed is not intractable due to javascript!!!")
                    except ElementNotVisibleException:
                        print("Hidden password field in page!!!")
                    except NoSuchElementException:
                        print("All fields seems to be empty!!!")
                except ElementNotInteractableException:
                        print("Password filed is not intractable due to JAVAscript!!!")
                except ElementNotVisibleException:
                    print("Hidden password input by CSS!!!")
            elif field[0] == 'radio':
                try:
                    self.driver.find_element(By.ID, field[2]).click()
                except NoSuchElementException:
                    print("ID field is blank!!")
                except ElementNotVisibleException:
                    print("Radio button is hidden!!!")
            else:
                print("Need to catch the type ",field[0])

        print('______________________________________________\n')

    
    def get_inputs(self):

        print('--------Inputs-------------')
        try:
            self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))
        except TimeoutException:
            pass
        inputs = self.driver.find_elements(By.TAG_NAME, 'input')
        input_details = []
        for y in range(len(inputs)):
            if inputs[y].get_attribute('type').strip() != 'hidden':
                if inputs[y].get_attribute('type').strip() != 'submit':
                   input_details.append((inputs[y].get_attribute('type'),inputs[y].get_attribute('name'),
                        inputs[y].get_attribute('id'))) 

        print("Total fields ",len(input_details))
        return input_details

    
    def Quit(self):
        self.driver.quit()



class Validation:
    
    def checkURL(self, url):
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

    
    def checkTEXT(self, msg):
        regex = re.compile(
            r'\w*(not found)\w*', re.IGNORECASE)
        return re.search(regex, msg) is not None



if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print("Enter the site to crawl:(Without https/http)")
        str = input()
    else:
        str = sys.argv[1]
    
    testURL = Validation()
    if testURL.checkURL(str):
        url = str
    else:
        url = "https://"+str
    
    if testURL.checkURL(url):
        obj = Link()
        try:
            obj.initDriver(url)
        finally:
            obj.Quit()        
    else:
        print("Invalid URL given!!!")