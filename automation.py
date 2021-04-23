from selenium import webdriver
import time

driver = webdriver.Chrome("") #Please Insert Your webdriver full Path 

driver.get(
    'https://www.youtube.com/')


Searchbox = driver.find_element_by_xpath('//*[@id="search"]')
Searchbox.send_keys('Runaway song') #Type what u wanna search
Search = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
Search.click()

time.sleep(1)

find = driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]')
find.click()
