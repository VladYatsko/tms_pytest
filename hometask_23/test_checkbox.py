from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestCheckbox:
    def test_checkbox(self, setup_browser):
        setup_browser.get('http://the-internet.herokuapp.com/dynamic_controls')
        WebDriverWait(setup_browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="checkbox"]')))
        WebDriverWait(setup_browser, 10) \
            .until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Remove"]'))).click()
        WebDriverWait(setup_browser, 10) \
            .until(EC.visibility_of_element_located((By.XPATH, '//p[text()="It\'s gone!"]')))
        assert WebDriverWait(setup_browser, 10)\
            .until_not(EC.visibility_of_element_located((By.XPATH, '//input[@type="checkbox"]')))
        assert setup_browser.find_element(By.XPATH, '//input[@type="text"][@disabled]').is_displayed()
        WebDriverWait(setup_browser, 10) \
            .until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Enable"]'))).click()
        WebDriverWait(setup_browser, 10) \
            .until(EC.visibility_of_element_located((By.XPATH, '//p[text()="It\'s enabled!"]')))
        assert setup_browser.find_element(By.XPATH, '//input[@type="text"]').is_enabled()
        