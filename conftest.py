import pytest
from selenium import webdriver
import requests
import paramiko


def pytest_addoption(parser):
    parser.addoption('--url', action='store', help='opencart url', default='http://localhost')
    parser.addoption('--browser', action='store', help='browser for tests', choices=['chrome', 'firefox', 'ie'], default='chrome')
    parser.addoption('--platform', action='store', help='platform for tests', choices=['windows', 'linux'], default='linux')
    parser.addoption('--executor', action='store', help='executor for tests', choices=['local', 'grid', 'cloud'], default='local')
    parser.addoption('--wait', action='store', help='wait', default=10)


@pytest.fixture
def browser(request):
    cl_browser = request.config.getoption('--browser')
    cl_executor = request.config.getoption('--executor')
    cl_wait = request.config.getoption('--wait')
    if cl_executor == 'grid':
        cl_platform = request.config.getoption('--platform')
        wd = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
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
            # options.add_argument('headless')
            wd = webdriver.Chrome(options=options)
    wd.wait = cl_wait
    # wd.implicitly_wait(wd.wait)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def random_product_name():
    return requests.get('http://names.drycodes.com/1').json()[0]


@pytest.fixture
def ssh_client():
    host = '192.168.241.130'
    user = 'root'
    secret = '1'
    port = 22
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    yield client
    client.close()
