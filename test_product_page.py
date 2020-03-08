from pages import ProductPage


def test_main_page(browser, base_url):
    browser.get(base_url + '/index.php?route=product/product&product_id=43')
    browser.find_elements_by_css_selector(ProductPage.PRODUCT_NAME)
    browser.find_elements_by_css_selector(ProductPage.PRODUCT_PRICE)
    browser.find_elements_by_css_selector(ProductPage.QUANTITY)
    browser.find_elements_by_css_selector(ProductPage.ADDTOCART_BUTTON)
    browser.find_elements_by_css_selector(ProductPage.BRAND_LINK)
