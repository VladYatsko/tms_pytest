from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, timeout=10)
        
    def open_page(self):
        self.driver.get(self.url)
        
    def find_presenting_element(self, locator) -> WebElement:
        return self.wait.until(ec.presence_of_element_located(locator))
        
    def find_presenting_elements(self, locator) -> list:
        return self.wait.until(ec.presence_of_all_elements_located(locator))
    
    def get_title(self):
        return self.driver.title
    
    def click_element(self, locator) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator)).click()
    
    def send_text(self, locator, value):
        return self.wait.until(ec.element_to_be_clickable(locator)).send_keys(value)
     
    def get_url(self):
        return self.driver.current_url
    
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    