from selenium.webdriver import ActionChains

from page_object.locators.home_page_locators import HomePageLocators
from page_object.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
    
    def home_page_is_expected(self):
        assert self.get_url() == HomePageLocators.URL
    
    def open_best_sellers(self):
        self.click_element(HomePageLocators.BEST_SELLERS)
        
    def add_to_cart(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_presenting_element(HomePageLocators.BLOUSE_GOOD))
        action.move_to_element(self.find_presenting_element(HomePageLocators.ADD_TO_CART))
        action.perform()
        self.click_element(HomePageLocators.ADD_TO_CART)
        
    def back_to_shopping(self):
        self.click_element(HomePageLocators.BACK_TO_SHOPPING_BUTTON)
        
    def proceed_to_checkout(self):
        self.click_element(HomePageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        
    def switch_to_popular(self):
        self.click_element(HomePageLocators.POPULAR_GOODS)
        
    def close_pop_up(self):
        self.click_element(HomePageLocators.CLOSE_WINDOW)
    
    def to_bucket_transition(self):
        self.click_element(HomePageLocators.BUCKET_TRANSITION)
        
    def to_login_transition(self):
        self.click_element(HomePageLocators.LOGIN_TRANSITION)