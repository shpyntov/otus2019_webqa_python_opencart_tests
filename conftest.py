import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url', action='store', help='opencart url', default='http://localhost')
    parser.addoption('--browser', action='store', help='browser for tests', choices=['chrome', 'firefox', 'ie'], default='chrome')
    parser.addoption('--platform', action='store', help='platform for tests', choices=['windows', 'linux'], default='windows')
    parser.addoption('--executor', action='store', help='executor for tests', choices=['local', 'grid', 'cloud'], default='local')


@pytest.fixture
def browser(request):
    cl_browser = request.config.getoption('--browser')
    cl_executor = request.config.getoption('--executor')
    if cl_executor == 'grid':
        cl_platform = request.config.getoption('--platform')
        wd = webdriver.Remote(command_executor='http://192.168.241.1:4444/wd/hub',
                              desired_capabilities={'browserName': cl_browser, 'platform': cl_platform})
    elif cl_executor == 'cloud':
        desired_cap = {
            'browser': 'Firefox',
            'browser_version': '74.0 beta',
            'os': 'Windows',
            'os_version': '7',
            'resolution': '1024x768',
            'name': 'Demo OpenCart Test'
        }

        wd = webdriver.Remote(
            command_executor='https://yurysh1:m4RXgUbtwsbpHSxazUL3@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap)
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
