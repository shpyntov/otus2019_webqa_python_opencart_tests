from pages import MainPage


def test_check_elements(browser, base_url):
    browser.get(base_url)
    browser.find_element_by_css_selector(MainPage.TOP_SLIDESHOW)
    browser.find_element_by_css_selector(MainPage.BOTTOM_SLIDESHOW)
    browser.find_element_by_css_selector(MainPage.FEATURED_BOX)
    browser.find_element_by_css_selector(MainPage.FEATURED_BOX_PRODUCT_LINK)
    browser.find_element_by_css_selector(MainPage.FOTTER_LINKS)
