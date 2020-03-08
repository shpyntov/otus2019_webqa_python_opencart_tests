from pages import AdminLoginPage


def test_main_page(browser, base_url):
    browser.get(base_url + 'admin')
    browser.find_elements_by_css_selector(AdminLoginPage.LOGIN_INPUT)
    browser.find_elements_by_css_selector(AdminLoginPage.PASS_INPUT)
    browser.find_elements_by_css_selector(AdminLoginPage.LOGIN_BUTTON)
    browser.find_elements_by_css_selector(AdminLoginPage.FORG_PASS_LINK)
    browser.find_elements_by_css_selector(AdminLoginPage.PAGE_TEXT)
