from selenium.webdriver.common.by import By


class LoginLocatorPage:
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN = (By.XPATH, "//input[@placeholder='Password']")
