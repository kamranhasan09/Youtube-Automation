# Please Install module = 'pip install selenium'
# and give path of web driver of ur web browser 

# Link to download web drivers👇👇
# Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox:	https://github.com/mozilla/geckodriver/releases
# Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

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
