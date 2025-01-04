from utils import allure
import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from appium import webdriver
from dotenv import load_dotenv


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    load_dotenv()
    login = os.getenv('BS_LOGIN')
    access_key = os.getenv('BS_KEY')
    remote_url = os.getenv('BS_URL')

    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # 'platformName': 'android',
        'platformVersion': '9.0',
        'deviceName': 'Samsung Galaxy S10',

        # Set URL of the application under test
        'app': 'bs://sample.app',

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # Set your access credentials
            'userName': login,
            'accessKey': access_key,
        }
    })

    browser.config.driver = webdriver.Remote(
        f'http://{remote_url}/wd/hub',
        options=options
    )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    session_id = browser.driver.session_id

    yield

    allure.add_screenshot(browser)
    allure.add_xml(browser)
    allure.add_video(session_id, login, access_key)

    browser.quit()
