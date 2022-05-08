from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sqlite3

def search():
    text = '키보드'
    page = 1

    option = Options()
    option.add_argument('no-sandbox')
    # option.add_argument('--headless')
    # browser = webdriver.Chrome('./chromedriver', options=option)
    browser = webdriver.Chrome('./chromedriver')


    browser.get('https://shopping.naver.com/home/p/index.naver')
    WebDriverWait(browser, 2).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'input[name=query]'))).send_keys(text+'\n')
    
    try:
        browser.find_element_by_class_name('filter_label_hit__31QIX').click()
    except:
       pass


    WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'div[class ^= basicList_info_area__]')))


    while page < 8:
        # 스크롤
        for i in range(13):
            browser.execute_script('window.scrollBy(0, window.innerHeight)')
            time.sleep(1)

        items = browser.find_elements_by_css_selector('li[class ^= basicList_item__2XT81]')

        for item in items:
            # 리뷰가 있는 것만
            try:
                item.find_element_by_css_selector('button[class^=ad_]')
                continue
            except:
                pass

            try:
                item.find_element_by_css_selector('a[class^=basicList_compare__3AjuT]')
                print('상품명:'+item.find_element_by_css_selector('a[class^=basicList_link__]').text)
                # print('가격:'+item.find_element_by_css_selector('span[class^=price_num__]').text)
                # print('리뷰 수:'+item.find_element_by_css_selector('em[class^=basicList_num__1yXM9]').text)
                # href = item.find_element_by_css_selector('a[class^=basicList_link__]').get_attribute('href')
                # print('주소:'+href)
            except:
                pass
        # 페이지 이동
        page += 1

        try:
            WebDriverWait(browser, 2).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div.pagination_num__-IkyP > a:nth-child({})'.format(page)))).click()
        except:
            pass
    time.sleep(100)
    browser.close()

# -------------------------------------------------------------------------------------------------------------------------------------------------


# 우선 한 페이지만 
def review():
    # 테스트
    url = 'https://cr.shopping.naver.com/adcr.nhn?x=Ymvx7CrdgjJ8TpaRwt6IvP%2F%2F%2Fw%3D%3DsG5trIjJn7GsYQ6j5bIVd6lg81ADxo3wUmSsxfhUQJ32TsjdUuseXhO5PK3WZnW9bOfNS5z4C7O3W4uSDK%2BqaJh4pza8ebIOIXPrPsGGS95ek6v2w9jBqMGR4TTsgYaQn%2FBJ5oXVSdspZwNGnFDAmiSQyT9qJw3Z0iHsamaElWfGp3%2BJcNEQcha96gwrv8km2Us%2BWH8m8CB3Y49dFMIFSZoBsJjzV%2F3vl5Lmd9HbkUGKGUUyLQ0szeEs9oKeNFnXtbzWLiMgcrU1%2B3rMXGLkB6MPqFcOD%2BKHcYoCGJ3ot6C0v%2BM6YRmoErl69WomQfkbS8LrWRGdZvlUvI0XjxLEaOlVd6Z%2BmZ5fvTALbBBPmfKLmnGLANk9TjQtjOEdf9xG%2FngH4ske%2FnUa4g%2B9FuaDUAD1nRJ4yoQ1ByXgZXYF4asUbNzLX1esQXuHm%2Fk%2F4c2IYdNQS9A16ct1blx%2FGOOOfqQp3GmZH8572EBGDELnqRN0Z2NyjP4RHbO%2BX82zfDKB8LL7LlxDed3495tvVWb67cYXf9fWCtx5Esbvzc4Jgr7ncXRFrRDD1gTfrQD7ZJ%2BHpxnIbgfPeu4QaB8hLM8%2FwJvPfTetPxxd9nfo%2BJy3GB21blyYSU2MWDvb2cOPGrAcmb9W0CxnmaioabDCB33lYGz6CFtWTAv3Npigb6bCCrGDAHHLyxgMfQRhyzOgszDDosvHhYcoDJQ5hF%2B%2FZW4XdmUHQIiXcF4qwUXZ2sX76wW8%3D&nvMid=20426740931&catId=50002933'
    # 리뷰많은 순
    url2 = 'https://search.shopping.naver.com/catalog/14761858336?query=%ED%82%A4%EB%B3%B4%EB%93%9C&NaPm=ct%3Dl2x163tk%7Cci%3D4a18cb218efaa30c178f6f74a292fc7180f5933b%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Dcc066fa11fbadb7751f188d6a33ac23a069e15b7'

 
    option = Options()
    option.add_argument('no-sandbox')
    # option.add_argument('--headless')
    # browser = webdriver.Chrome('./chromedriver', options=option)
    browser = webdriver.Chrome('./chromedriver')
    browser.get(url2)

    with open('test_all.txt', 'w', encoding='utf-8') as f:
        page = 1
        chk_page = 1
        while chk_page < 92:
            try:
                WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="snb"]/ul/li[4]/a'))).click()
            except:
                pass
            # for i in range(6):
            #     browser.execute_script('window.scrollBy(0, window.innerHeight)')
            #     time.sleep(1)
            

            items = browser.find_elements_by_css_selector('div[class^=reviewItems_review_text__2Bwpa]')

            for item in items:
                try:
                    # print(item.find_element_by_css_selector('p[class^=reviewItems_text__XIsTc]').text)    
                    # print()
                    data = item.find_element_by_css_selector('p[class^=reviewItems_text__XIsTc]').text
                    f.write(data)
                except:
                    pass
            
            chk_page += 1
            page += 1
            if page % 10 == 1:
                WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'div.review_section_review__1hTZD >  div.pagination_pagination__2M9a4 > a.pagination_next__3ycRH'))).click()
                page = page % 10 
            else:
                try:     
                    WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'div.review_section_review__1hTZD >  div.pagination_pagination__2M9a4 > a:nth-child({})'.format(page)))).click()
                except:
                    pass

    time.sleep(100)

# ---------------------------------------------------------------------------------------------------------------------------------------------------
review()