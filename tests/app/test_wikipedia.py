from utils import allure
from utils.allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search():

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Appium")

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_open_article_after_search():
    with allure.step('Открываем меню'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/menu_overflow_button")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Tesla")

    with allure.step('Заходим в настройки'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text('Tesla')).should(be.visible)
