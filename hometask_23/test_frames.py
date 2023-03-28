from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestFrames:
    def test_frames(self, setup_browser):
        setup_browser.get('http://the-internet.herokuapp.com/iframe')
        setup_browser.switch_to.frame(WebDriverWait(setup_browser, timeout=10)
                                      .until(ec.presence_of_element_located((By.TAG_NAME, 'iframe'))))
        assert WebDriverWait(setup_browser, timeout=10) \
                   .until(ec.presence_of_element_located((By.TAG_NAME, 'body'))).text == 'Your content goes here.'
