from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from webdriverproject.browser import Browser, Config
from webdriverproject.conditions import have

browser = Browser(
    webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
    Config(timeout=3, base_url='https://ecosia.org')
)


def test_number_of_pull_requests():
    browser.open('/')
    query = '[name=q]'

    # WHEN
    browser.type(query, value='selene yashaka pulls' + Keys.ENTER)
    browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')

    # THEN
    browser.should(have.number_of_elements('[id^=issue_]:not([id$=_link])', value=9))

    browser.quit()
