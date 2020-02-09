import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", action="store", help="opencart url")
    parser.addoption("--browser", action="store", help="Browser for tests")


@pytest.fixture
def browser(request):
    cl_option_browser = request.config.getoption('--browser')
    if cl_option_browser == 'ie':
        wd = webdriver.Ie()
    elif cl_option_browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = True
        wd = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        wd = webdriver.Chrome(options=options)

    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')
