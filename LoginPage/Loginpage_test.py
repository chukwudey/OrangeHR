import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from LoginLocator.LoginLocator_test import LoginLocatorPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def Login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.USERNAME))
        enter_username.send_keys(username)
        time.sleep(3)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(3)

    def click_login(self):
        click_login = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.LOGIN))
        click_login.click()

        time.sleep(3)


