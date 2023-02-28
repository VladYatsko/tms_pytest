from selenium.webdriver.common.by import By


class TestLocators:
    def test_button_search(self, setup_browser):
        setup_browser.implicitly_wait(10)
        setup_browser.get('https://baraholka.onliner.by/')
        assert 'Разместить объявление' in \
               setup_browser.find_element(By.XPATH, '//a[@href="/fleamarketposting.php"]').text
        
    def test_video_cards_search(self, setup_browser):
        setup_browser.implicitly_wait(10)
        setup_browser.get('https://baraholka.onliner.by/')
        assert setup_browser.find_element(By.XPATH, '//a[text()="Видеокарты"]//following-sibling::sup').is_displayed()
        
    def test_dresses__search(self, setup_browser):
        setup_browser.implicitly_wait(10)
        setup_browser.get('https://baraholka.onliner.by/')
        assert setup_browser.find_element(By.XPATH, '//a[text()="Платья"]//following-sibling::sup').is_displayed()
