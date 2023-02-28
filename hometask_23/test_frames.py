from selenium.webdriver.common.by import By


class TestFrames:
    def test_frames(self, setup_browser):
        setup_browser.get('http://the-internet.herokuapp.com/iframe')
        setup_browser.switch_to.frame(setup_browser.find_element(By.TAG_NAME, 'iframe'))
        assert setup_browser.find_element(By.TAG_NAME, 'body').text == 'Your content goes here.'
