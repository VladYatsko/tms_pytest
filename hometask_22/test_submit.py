import time
from selenium.webdriver.common.by import By


class TestSubmit:
    def test_positive_submit(self, setup_browser):
        setup_browser.get('https://ultimateqa.com/filling-out-forms/')
        setup_browser.maximize_window()
        time.sleep(3)
        setup_browser.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys('Any name')
        setup_browser.find_element(By.XPATH, "//textarea[@placeholder='Message']").send_keys('Any message')
        setup_browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        assert setup_browser.find_element(By.XPATH, "//p[text()='Thanks for contacting us']").text ==\
               'Thanks for contacting us'
        
    def test_without_message(self, setup_browser):
        setup_browser.get('https://ultimateqa.com/filling-out-forms/')
        setup_browser.maximize_window()
        time.sleep(3)
        setup_browser.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys('Any name')
        setup_browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        assert setup_browser.find_element(By.XPATH, '//div/ul/li[text()="Message"]').text == 'Message'
    
    def test_without_name(self, setup_browser):
        setup_browser.get('https://ultimateqa.com/filling-out-forms/')
        setup_browser.maximize_window()
        time.sleep(3)
        setup_browser.find_element(By.XPATH, "//textarea[@placeholder='Message']").send_keys('Any message')
        setup_browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        assert setup_browser.find_element(By.XPATH, '//div/ul/li[text()="Name"]').text == 'Name'
        