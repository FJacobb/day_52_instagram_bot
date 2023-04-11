import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Ig:
    def __init__(self):
        self.driver = webdriver.Chrome("c:/Users/festu/OneDrive/Documents/chromedriver.exe")
        self.driver.maximize_window()
        self.username = os.environ.get("INSTAGRAM_USERNAME")
        self.password = os.environ.get("INSTAGRAM_PASSWORD")
    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(10)
        user = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        user.send_keys(self.username)
        passwd = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        passwd.send_keys(self.password)
        passwd.send_keys(Keys.ENTER)
        time.sleep(20)

    def find_followers(self, name):
        search = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[2]/div/div")
        search.click()
        time.sleep(5)
        search_input = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input")
        search_input.send_keys(name)
        search_input.send_keys(Keys.ENTER)
        time.sleep(10)

        list = self.driver.find_elements(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div")
        list[0].click()
        time.sleep(10)
    def follow(self):
        followers = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]")
        followers.click()
        time.sleep(10)
        follow = self.driver.find_elements(By.XPATH, value="/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[3]/div/button/div/div")
        for x in follow:
            if x.text == "Follow":
                x.click()
                time.sleep(1)

        # scroll = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)

        time.sleep(20)




