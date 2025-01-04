from utils import allure
import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from appium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # 'platformName': 'android',
        'platformVersion': '8.0',
        'deviceName': 'Samsung Galaxy S9',

        # Set URL of the application under test
        'app': 'bs://sample.app',

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # Set your access credentials
            'userName': "glreb_PUhTNr",
            'accessKey': "Wrea2X6gfeEuumMkC7dD",
        }
    })

    browser.config.driver = webdriver.Remote(
        'http://hub.browserstack.com/wd/hub',
        options=options
    )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    session_id = browser.driver.session_id

    allure.add_screenshot(browser)
    allure.add_xml(browser)
    allure.add_video(session_id, "glreb_PUhTNr", "Wrea2X6gfeEuumMkC7dD")

    yield

    browser.quit()
