from pages import AdminPage
from pages import AdminLoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from random import randint


def test_add_new_product(browser, base_url, random_product_name):
    wait = WebDriverWait(browser, browser.wait)
    browser.get(base_url + '/admin')

    browser.find_element_by_css_selector(AdminLoginPage.LOGIN_INPUT).send_keys('admin')
    browser.find_element_by_css_selector(AdminLoginPage.PASS_INPUT).send_keys('admin')
    browser.find_element_by_css_selector(AdminLoginPage.LOGIN_BUTTON).click()

    browser.find_element_by_css_selector(AdminPage.CATALOG_MENU_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminPage.PRODUCTS_MENU_BUTTON)))
    browser.find_element_by_css_selector(AdminPage.PRODUCTS_MENU_BUTTON).click()

    browser.find_element_by_css_selector(AdminPage.ADD_NEW_PRODUCT).click()
    browser.find_element_by_css_selector(AdminPage.NEW_PRODUCT_NAME).send_keys(random_product_name)
    browser.find_element_by_css_selector(AdminPage.NEW_PRODUCT_META).send_keys(random_product_name)
    browser.find_element_by_css_selector(AdminPage.DATA_TAB).click()
    browser.find_element_by_css_selector(AdminPage.NEW_PRODUCT_MODEL).send_keys(randint(1, 100))
    browser.find_element_by_css_selector(AdminPage.SAVE_NEW_PRODUCT).click()

    while True:
        products = browser.find_elements_by_css_selector(AdminPage.PRODUCT_NAME_IN_TABLE)
        for product in products:
            if random_product_name == product.text:
                return True
        if browser.find_elements_by_link_text('>') == []:
            return False
        else:
            browser.find_element_by_link_text('>').click()