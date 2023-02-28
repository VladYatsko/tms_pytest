from selenium.webdriver.common.by import By


class TestClicker:
    def test_click_via_xpath(self, setup_browser):
        setup_browser.implicitly_wait(10)
        setup_browser.get('https://ultimateqa.com/complicated-page/')
        setup_browser.find_element(By.XPATH, '//a[@class="et_pb_button et_pb_button_4 et_pb_bg_layout_light"]').click()
        assert setup_browser.find_element(By.XPATH, '//a[@class="et_pb_button et_pb_button_4 et_pb_bg_layout_light"]')\
            .is_displayed()
        
    def test_click_via_css(self, setup_browser):
        setup_browser.implicitly_wait(10)
        setup_browser.get('https://ultimateqa.com/complicated-page/')
        setup_browser.find_element(By.CSS_SELECTOR, 'a.et_pb_button_4').click()
        assert setup_browser.find_element(By.CSS_SELECTOR, 'a.et_pb_button_4') \
            .is_displayed()
        
    def test_click_via_class(self, setup_browser):
        setup_browser.implicitly_wait(10)
        setup_browser.get('https://ultimateqa.com/complicated-page/')
        setup_browser.find_element(By.CLASS_NAME, 'et_pb_button_4').click()
        assert setup_browser.find_element(By.CLASS_NAME, 'et_pb_button_4') \
            .is_displayed()
