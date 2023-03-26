from selenium.webdriver.common.by import By


class BucketPageLocators:
    URL = 'http://automationpractice.pl/index.php?controller=order'
    EMPTY_CART = (By.XPATH, "//p[text()='Your shopping cart is empty.']")
    QUANTITY_FIELD = (By.XPATH, "//input[@type='text']")
    SUBTRACT_QUANTITY = (By.XPATH, "//a[@title='Subtract']")
    ADD_QUANTITY = (By.XPATH, "//a[@title='Add']")
    DELETE_ITEM = (By.XPATH, "//i[@class='icon-trash']")
    