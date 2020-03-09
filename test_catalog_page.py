from pages import CatalogPage


def test_check_elements(browser, base_url):
    browser.get(base_url + '/index.php?route=product/category&path=18')
    browser.find_element_by_css_selector(CatalogPage.CATALOG_NAME)
    browser.find_element_by_css_selector(CatalogPage.CATALOG_TEXT)
    browser.find_element_by_css_selector(CatalogPage.PRODUCT_PRICE)
    browser.find_element_by_css_selector(CatalogPage.PRODUCT_BUTTONS)
    browser.find_element_by_css_selector(CatalogPage.PRODUCT_LINK)
