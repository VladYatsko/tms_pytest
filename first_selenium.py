from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web():
    chrome = webdriver.Chrome()
    url = 'https://www.google.com/'
    chrome.get(url=url)
    chrome.maximize_window()
    if chrome.find_element(By.XPATH, '//*[@id="L2AGLb"]/div'):
        chrome.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
    search_box = chrome.find_element(By.NAME, 'q')
    search_box.send_keys('Python 3.10')
    search_box.submit()
    assert 'Python 3.10' in chrome.title
    chrome.close()
    