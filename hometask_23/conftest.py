import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.close()
    