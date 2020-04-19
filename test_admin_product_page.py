from pages import AdminPage
from pages import AdminLoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from random import randint
import selenium.common.exceptions as EXC


def test_add_new_product(browser, base_url, random_product_name):
    # preparing
    wait = WebDriverWait(browser, browser.wait)
    browser.get(base_url + '/admin')
    # login to admin page
    browser.find_element_by_css_selector(AdminLoginPage.LOGIN_INPUT).send_keys('admin')
    browser.find_element_by_css_selector(AdminLoginPage.PASS_INPUT).send_keys('admin')
    browser.find_element_by_css_selector(AdminLoginPage.LOGIN_BUTTON).click()
    # goto a products page
    browser.find_element_by_css_selector(AdminPage.CATALOG_MENU_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminPage.PRODUCTS_MENU_BUTTON)))
    browser.find_element_by_css_selector(AdminPage.PRODUCTS_MENU_BUTTON).click()
    # add a new random product
    browser.find_element_by_css_selector(AdminPage.ADD_PRODUCT).click()
    browser.find_element_by_css_selector(AdminPage.PRODUCT_NAME).send_keys(random_product_name)
    browser.find_element_by_css_selector(AdminPage.PRODUCT_META).send_keys(random_product_name)
    browser.find_element_by_css_selector(AdminPage.DATA_TAB).click()
    browser.find_element_by_css_selector(AdminPage.PRODUCT_MODEL).send_keys(randint(1, 100))
    browser.find_element_by_css_selector(AdminPage.SAVE_PRODUCT).click()
    # check that the new product in the table
    while True:
        products = browser.find_elements_by_css_selector(AdminPage.PRODUCT_NAMES_IN_TABLE)
        for product in products:
            if random_product_name == product.text:
                assert True
        if browser.find_elements_by_link_text('>') == []:
            assert False
        else:
            browser.find_element_by_link_text('>').click()


def test_remove_product(browser, base_url):
    # preparing
    wait = WebDriverWait(browser, browser.wait)
    browser.get(base_url + '/admin')
    # login to admin page
    browser.find_element_by_css_selector(AdminLoginPage.LOGIN_INPUT).send_keys('admin')
    browser.find_element_by_css_selector(AdminLoginPage.PASS_INPUT).send_keys('admin')
    browser.find_element_by_css_selector(AdminLoginPage.LOGIN_BUTTON).click()
    # goto a products page
    browser.find_element_by_css_selector(AdminPage.CATALOG_MENU_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminPage.PRODUCTS_MENU_BUTTON)))
    browser.find_element_by_css_selector(AdminPage.PRODUCTS_MENU_BUTTON).click()
    # remove random product
    products = browser.find_elements_by_css_selector(AdminPage.PRODUCT_ROWS_IN_TABLE)
    removed_product = products.pop(randint(0, len(products)-1))
    removed_product_name = removed_product.find_element_by_css_selector(AdminPage.PRODUCT_NAMES_IN_TABLE).text
    removed_product.find_element_by_css_selector(AdminPage.PRODUCT_CHECKBOXES_IN_TABLE).click()
    browser.find_element_by_css_selector(AdminPage.REMOVE_PRODUCT).click()
    try:
        wait.until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert.accept()
    except EXC.TimeoutException:
        print("no alert")
    finally:
        # check that the product not in the table
        while True:
            products = browser.find_elements_by_css_selector(AdminPage.PRODUCT_NAMES_IN_TABLE)
            for product in products:
                if removed_product_name == product.text:
                    assert False
            if browser.find_elements_by_link_text('>') == []:
                assert True
            else:
                browser.find_element_by_link_text('>').click()


def test_edit_product(browser, base_url, random_product_name):
    # preparing
    wait = WebDriverWait(browser, browser.wait)
    browser.get(base_url + '/admin')
    # login to admin page
    browser.find_element_by_css_selector(AdminLoginPage.LOGIN_INPUT).send_keys('admin')
    browser.find_element_by_css_selector(AdminLoginPage.PASS_INPUT).send_keys('admin')
    browser.find_element_by_css_selector(AdminLoginPage.LOGIN_BUTTON).click()
    # goto a products page
    browser.find_element_by_css_selector(AdminPage.CATALOG_MENU_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminPage.PRODUCTS_MENU_BUTTON)))
    browser.find_element_by_css_selector(AdminPage.PRODUCTS_MENU_BUTTON).click()
    # edit random product
    products = browser.find_elements_by_css_selector(AdminPage.PRODUCT_ROWS_IN_TABLE)
    edited_product = products.pop(randint(0, len(products)-1))
    edited_product.find_element_by_css_selector(AdminPage.EDIT_BUTTONS_IN_TABLE).click()
    browser.find_element_by_css_selector(AdminPage.PRODUCT_NAME).clear()
    browser.find_element_by_css_selector(AdminPage.PRODUCT_NAME).send_keys(random_product_name)
    browser.find_element_by_css_selector(AdminPage.SAVE_PRODUCT).click()
    assert AdminPage.SUCCESS_EDIT_ALERT_TEXT in wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminPage.ALERT))).text
    # check that the new product in the table
    while True:
        products = browser.find_elements_by_css_selector(AdminPage.PRODUCT_NAMES_IN_TABLE)
        for product in products:
            if random_product_name == product.text:
                assert True
        if browser.find_elements_by_link_text('>') == []:
            assert False
        else:
            browser.find_element_by_link_text('>').click()
