import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", action="store", help="opencart url", default='http://localhost')
    parser.addoption("--browser", action="store", help="browser for tests", choices=["chrome", "firefox", 'ie'], default='chrome')
    parser.addoption("--platform", action="store", help="platform for tests", choices=["windows", "linux"], default='windows')
    parser.addoption("--executor", action="store", help="executor for tests", choices=["local", "grid"], default='local')


@pytest.fixture
def browser(request):
    cl_browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    if executor == 'grid':
        pass
    else:
        if cl_browser == 'ie':
            wd = webdriver.Ie()
        elif cl_browser == 'firefox':
            options = webdriver.FirefoxOptions()
            options.headless = True
            wd = webdriver.Firefox(options=options)
        elif cl_browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            wd = webdriver.Chrome(options=options)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')
