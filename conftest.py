import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", action="store", help="opencart url")
    parser.addoption("--browser", action="store", help="browser for tests")


@pytest.fixture
def browser(request):
    cl_browser = request.config.getoption('--browser')
    if cl_browser == 'ie':
        wd = webdriver.Ie()
    elif cl_browser == 'firefox':
        options = webdriver.FirefoxOptions()
        # options.headless = True
        wd = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        wd = webdriver.Chrome(options=options)

    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def base_url(request):
    cl_base_url = request.config.getoption('--url')
    if cl_base_url == None:
        return 'http://localhost'
    else:
        return cl_base_url
