from selenium.webdriver.common.by import By


class LoginPageLocators:
    URL = 'http://automationpractice.pl/index.php?controller=authentication&back=my-account'
    EMAIL_CREATE = (By.XPATH, "//input[@id='email_create']")
    CREATE_BUTTON = (By.XPATH, "//button[@id='SubmitCreate']")
    REGISTERED_EMAIL = (By.XPATH, "//input[@id='email']")
    REGISTERED_PASSWORD = (By.XPATH, "//input[@id='passwd']")
    LOGIN_BUTTON = (By.XPATH, "//button[id='SubmitLogin']")
    