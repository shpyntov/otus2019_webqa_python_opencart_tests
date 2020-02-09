def test_is_opened(browser, base_url):
    browser.get(base_url)
    assert browser.title == 'Your Store'
