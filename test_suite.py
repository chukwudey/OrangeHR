import time

import pytest
from selenium import webdriver

from LoginPage.Loginpage_test import LoginPage
from config.config import Config


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.Login_url(Config.BaseUrl)
    return login_page


time.sleep(5)


def test_login_page_automation_hrm(login):
    login.enter_username(Config.Username)
    login.enter_password(Config.Password)
    login.click_login()


