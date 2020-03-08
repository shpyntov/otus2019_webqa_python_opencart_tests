from pages import CatalogPage


def test_main_page(browser, base_url):
    browser.get(base_url + '/index.php?route=product/category&path=18')
    browser.find_elements_by_css_selector(CatalogPage.CATALOG_NAME)
    browser.find_elements_by_css_selector(CatalogPage.CATALOG_TEXT)
    browser.find_elements_by_css_selector(CatalogPage.PRODUCT_PRICE)
    browser.find_elements_by_css_selector(CatalogPage.PRODUCT_BUTTONS)
    browser.find_elements_by_css_selector(CatalogPage.PRODUCT_LINK)
