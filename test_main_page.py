from pages import MainPage


def test_main_page(browser, base_url):
    browser.get(base_url)
    browser.find_elements_by_css_selector(MainPage.TOP_SLIDESHOW)
    browser.find_elements_by_css_selector(MainPage.BOTTOM_SLIDESHOW)
    browser.find_elements_by_css_selector(MainPage.FEATURED_BOX)
    browser.find_elements_by_css_selector(MainPage.FEATURED_BOX_PRODUCT_LINK)
    browser.find_elements_by_css_selector(MainPage.FOTTER_LINKS)
