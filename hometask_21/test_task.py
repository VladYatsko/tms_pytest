from selenium.webdriver.common.by import By


class TestTask:
    def test_user_login(self, setup_browser):
        setup_browser.implicitly_wait(10)
        setup_browser.get('https://thedemosite.co.uk/savedata.php')
        setup_browser.find_element(By.XPATH, '//input[@name="username"]').send_keys("User")
        setup_browser.find_element(By.XPATH, '//input[@name="password"]').send_keys("Pass")
        setup_browser.find_element(By.XPATH, '//input[@value="save"]')
        assert setup_browser.find_element(By.XPATH, '//input[@name="username"]').text == ''
        
    def test_form_filling(self, setup_browser):
        setup_browser.implicitly_wait(10)
        setup_browser.get('https://demoqa.com/text-box')
        setup_browser.find_element(By.XPATH, '//input[@id="userName"]').send_keys("User Name")
        setup_browser.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys("yatsko.vladislav@gmail.com")
        setup_browser.find_element(By.XPATH, '//textarea[@id="currentAddress"]').send_keys("current addr")
        setup_browser.find_element(By.XPATH, '//textarea[@id="permanentAddress"]').send_keys("perm addr")
        setup_browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
        assert setup_browser.find_element(By.CSS_SELECTOR, 'div.border > p#name').is_displayed()
        