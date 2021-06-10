from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sec
from bs4 import BeautifulSoup as bs
IG_URL = 'http://instagram.com'


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='geckodriver.exe')

    def go_login_page(self):
        self.driver.get(IG_URL)
        sleep(5)
        # self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()

    def login(self):
        un_ide = WebDriverWait(self.driver, 20)
        un_id = un_ide.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')))

        # un_id = self.driver.find_element_by_css_selector
        # ('div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        un_id.click()
        un_id.send_keys(sec.un)

        pw_id = self.driver.find_element_by_css_selector(
            'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        pw_id.click()
        pw_id.send_keys(sec.pw)

        btn = self.driver.find_element_by_css_selector('.L3NKy > div:nth-child(1)')
        btn.click()
        sleep(20)

        # self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        # sleep(10)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(5)

    def like_photo(self, hashtag, amount):
        hashtag_url = 'https://www.instagram.com//explore/tags/' + hashtag
        self.driver.get(hashtag_url)
        sleep(3)
        self.driver.find_element_by_class_name('v1Nh3').click()
        i = 1
        while i <= amount:
            sleep(3)
            btn_like = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
            btn_like.click()
            sleep(1)
            self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            i += 1

    def get_folowers(self, page_id):

        page_url = 'https://www.instagram.com/' + page_id
        self.driver.get(page_url)

        followers_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')))
        followers_btn.click()
        sleep(3)

        pup = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))

        last_height, current_height = 0, 1

        while last_height != current_height:
            sleep(2)

            last_height = current_height

            current_height = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);return 
            arguments[0].scrollHeight;""", pup)

    def get_followers_number(self, page_id):

        page_url = 'https://www.instagram.com/' + page_id
        self.driver.get(page_url)

        page_content = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
        slfw = bs(page_content.get_attribute('innerHTML'), 'html.parser')
        num = slfw.findAll('span', {'class': 'g47SY'})
        post_num = num[0].getText()
        followers_num = num[1].getText()
        following_num = num[2].getText()
        print(post_num, followers_num, following_num)


if __name__ == '__main__':
    bt = Bot()
    bt.go_login_page()
    bt.login()
    bt.like_photo('python', 30)
    # bt.get_followers_number('bitcoin.info')
