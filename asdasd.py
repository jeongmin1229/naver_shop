import os
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

text = '삼겹살'

option = Options()
# option.add_argument('no-sandbox')
# option.add_argument('--headless')
# browser = webdriver.Chrome('./chromedriver', options=option)

browser = webdriver.Chrome('./chromedriver')
wait = WebDriverWait(browser, 3)



browser.get('https://search.shopping.naver.com/search/all?query='+text+'&frm=NVSHATC')
browser.implicitly_wait(3)
browser.find_element_by_class_name('filter_label_hit__31QIX').click()

soup = BeautifulSoup(browser.page_source, 'html.parser')


# browser.close()

