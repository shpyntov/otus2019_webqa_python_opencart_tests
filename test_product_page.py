from pages import ProductPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.common.exceptions as EXC


def test_check_elements(browser, base_url):
    browser.get(base_url + '/index.php?route=product/product&product_id=43')
    wait = WebDriverWait(browser, browser.wait)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ProductPage.PRODUCT_NAME)))
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ProductPage.PRODUCT_PRICE)))
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ProductPage.QUANTITY)))
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ProductPage.ADDTOCART_BUTTON)))
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ProductPage.BRAND_LINK)))
    except EXC.TimeoutException:
        assert False
