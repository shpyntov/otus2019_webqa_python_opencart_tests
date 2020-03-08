from pages import SearchPage


def test_main_page(browser, base_url):
    browser.get(base_url + '/index.php?route=product/search')
    browser.find_elements_by_css_selector(SearchPage.SEARCH_INPUT)
    browser.find_elements_by_css_selector(SearchPage.CATEGOTY_SELECT)
    browser.find_elements_by_css_selector(SearchPage.SEARCH_BUTTON)
    browser.find_elements_by_css_selector(SearchPage.IN_CATEGORIES_CHECKBOX)
    browser.find_elements_by_css_selector(SearchPage.IN_DESC_CHECKBOX)
