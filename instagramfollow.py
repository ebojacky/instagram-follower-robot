from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

URL_INSTA = "https://www.instagram.com/"
MY_USER = "***"
MY_PASS = "***"
SIMILAR_ACCOUNT = "https://www.instagram.com/**ghana/"


class InstaFollower:
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe")

    def login(self):
        chrome = "chromedriver_win32/chromedriver.exe"
        self.browser.get(URL_INSTA)
        sleep(5)

        user = self.browser.find_element(value="username", by=By.NAME)
        user.send_keys(MY_USER)
        user.send_keys(Keys.ENTER)

        passwd = self.browser.find_element(value="password", by=By.NAME)
        passwd.send_keys(MY_PASS)
        passwd.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        self.browser.get(SIMILAR_ACCOUNT)
        sleep(5)

        followers = self.browser.find_element(value="div ul li a", by=By.CSS_SELECTOR)
        followers.click()
        sleep(5)

        popup = self.browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]'
        )

        i = 0
        while True:
            self.browser.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                popup)
            sleep(1)

            i += 1

            if i > 10:
                break

    def follow(self):
        buttons = self.browser.find_elements(value="li button",
                                             by=By.CSS_SELECTOR)

        for button in buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                button_cancel = \
                    self.browser.find_element(by=By.XPATH,
                                              value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div['
                                                    '2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div['
                                                    '3]/button[2]')
                button_cancel.click()
                sleep(1)


my_insta = InstaFollower()
my_insta.login()
my_insta.find_followers()
my_insta.follow()
