from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from page_object.locators.login_page_locators import LoginPageLocators
from page_object.pages.base_page import BasePage
from page_object.generator.generator import generated_data


class LoginPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
    
    def login_page_is_expected(self):
        assert self.get_url() == LoginPageLocators.URL
    
    def proceed_to_account_creation(self):
        created_data = next(generated_data())
        email = created_data.email
        self.send_text(LoginPageLocators.EMAIL_CREATE, email)
        self.click_element(LoginPageLocators.CREATE_BUTTON)
        
    def login_to_website(self):
        created_data = next(generated_data())
        email = created_data.email
        password = created_data.password
        self.send_text(LoginPageLocators.REGISTERED_EMAIL, email)
        self.send_text(LoginPageLocators.REGISTERED_PASSWORD, password)
        action = ActionChains(self.driver)
        action.key_down(Keys.TAB).perform()
        action.key_up(Keys.TAB).perform()
        action.key_down(Keys.TAB).perform()
        action.key_up(Keys.TAB).perform()
        action.key_down(Keys.ENTER).perform()
        action.key_up(Keys.ENTER).perform()
    
    def is_not_logged_in(self):
        assert self.find_presenting_element(LoginPageLocators.EMAIL_CREATE).is_displayed() is True
        