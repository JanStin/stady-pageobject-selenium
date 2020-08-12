from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def can_add_product_to_basket(self):
        add_product_buttton = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        add_product_buttton.click()

