from hometask_25.tests.bucket_page import BucketPage
from hometask_25.tests.bucket_page_locators import BucketPageLocators
from hometask_25.tests.home_page import HomePage
from hometask_25.tests.home_page_locators import HomePageLocators
from pytest_bdd import scenarios, given, when, then


scenarios('../features/transition.feature')


@given('User opens home page')
def open_home_page(driver):
    home_page = HomePage(driver, HomePageLocators.URL)
    home_page.open_page()
    home_page.home_page_is_expected()
    

@when('User clicks bucket button')
def redirection_to_bucket(driver):
    home_page = HomePage(driver, HomePageLocators.URL)
    home_page.to_bucket_transition()
    
    
@then('User is redirected')
def is_redirected(driver):
    bucket_page = BucketPage(driver, BucketPageLocators.URL)
    bucket_page.bucket_page_is_expected()
    