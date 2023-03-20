from page_object.locators.bucket_page_locators import BucketPageLocators
from page_object.pages.base_page import BasePage


class BucketPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        
    def bucket_page_is_expected(self):
        assert self.get_url() == BucketPageLocators.URL
    
    def bucket_is_empty(self) -> bool:
        return self.find_presenting_element(BucketPageLocators.EMPTY_CART).text == 'Your shopping cart is empty.'
    
    