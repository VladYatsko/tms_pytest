from selenium.webdriver.common.by import By


class HomePageLocators:
    URL = 'http://automationpractice.pl/index.php'
    POPULAR_GOODS = (By.XPATH, "//a[@href='#homefeatured']")
    BEST_SELLERS = (By.XPATH, "//a[@href='#blockbestsellers']")
    BLOUSE_GOOD = (By.XPATH, "//a[@title='Blouse']")
    ADD_TO_CART = (By.XPATH, "//a[@title='Add to cart']")
    BACK_TO_SHOPPING_BUTTON = (By.XPATH, "//span[@title='Continue shopping']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[@title='Proceed to checkout']")
    CLOSE_WINDOW = (By.XPATH, "//span[@title='Close window']")
    LOGIN_TRANSITION = (By.XPATH, "//a[@class='login']")
    BUCKET_TRANSITION = (By.XPATH, "//a//b")
    