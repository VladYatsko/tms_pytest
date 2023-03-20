from page_object.locators.bucket_page_locators import BucketPageLocators
from page_object.locators.home_page_locators import HomePageLocators
from page_object.locators.login_page_locators import LoginPageLocators
from page_object.pages.bucket_page import BucketPage
from page_object.pages.home_page import HomePage
from page_object.pages.login_page import LoginPage


class TestPage:
    def test_transition_home_to_bucket(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        bucket_page = BucketPage(driver, BucketPageLocators.URL)
        home_page.open_page()
        home_page.home_page_is_expected()
        home_page.to_bucket_transition()
        bucket_page.bucket_page_is_expected()

    def test_transition_to_login(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        login_page = LoginPage(driver, LoginPageLocators.URL)
        home_page.open_page()
        home_page.home_page_is_expected()
        home_page.to_login_transition()
        login_page.login_page_is_expected()
        
    def test_adding_product(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        bucket_page = BucketPage(driver, BucketPageLocators.URL)
        home_page.open_page()
        home_page.home_page_is_expected()
        home_page.open_best_sellers()
        home_page.add_to_cart()
        home_page.close_pop_up()
        home_page.to_bucket_transition()
        bucket_page.bucket_page_is_expected()
        assert bucket_page.bucket_is_empty() is False
    
    def test_bucket_is_empty(self, driver):
        bucket_page = BucketPage(driver, BucketPageLocators.URL)
        bucket_page.open_page()
        bucket_page.bucket_page_is_expected()
        assert bucket_page.bucket_is_empty() is True
        
    def test_user_is_not_logged_in(self, driver):
        login_page = LoginPage(driver, LoginPageLocators.URL)
        login_page.open_page()
        login_page.login_page_is_expected()
        login_page.is_not_logged_in()
        
    def test_user_cant_login_with_random_data(self, driver):
        login_page = LoginPage(driver, LoginPageLocators.URL)
        login_page.open_page()
        login_page.login_page_is_expected()
        login_page.login_to_website()
        login_page.is_not_logged_in()
