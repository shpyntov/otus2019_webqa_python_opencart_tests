from pages import ProductPage


def test_check_elements(browser, base_url):
    browser.get(base_url + '/index.php?route=product/product&product_id=43')
    browser.find_element_by_css_selector(ProductPage.PRODUCT_NAME)
    browser.find_element_by_css_selector(ProductPage.PRODUCT_PRICE)
    browser.find_element_by_css_selector(ProductPage.QUANTITY)
    browser.find_element_by_css_selector(ProductPage.ADDTOCART_BUTTON)
    browser.find_element_by_css_selector(ProductPage.BRAND_LINK)
