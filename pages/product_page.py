from .base_page import BasePage
from .locators import ProductPageLocators
import re

class ProductPage(BasePage): 
    def can_add_product_to_basket(self):
        add_product_buttton = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        add_product_buttton.click()
        self.solve_quiz_and_get_code()
        self.should_be_quality_price()
        self.should_be_quality_name()
        
    def should_be_quality_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text 
        price_after = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_AFTER_ADD_MESSAGE).text 
        assert price == price_after, "Разная цена. В товаре - {price}. В сообщении корзины - {price_after}"

    def should_be_quality_name(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text 
        name_after = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_AFTER_ADD_MESSAGE).text 
        result = re.findall(name, name_after)
        assert len(result) == 1, "Разные назавания продукта. В товаре - {name}. В сообщении корзины - {name_after}"