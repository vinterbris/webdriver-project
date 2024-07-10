from selenium.webdriver import Keys

from webdriverproject.browser import Browser
from webdriverproject.conditions import number_of_elements

def test_number_of_pull_requests():
    browser = Browser()

    browser.open('https://ecosia.org')
    query = '[name=q]'

    # WHEN
    browser.type(query, value='selene yashaka pulls' + Keys.ENTER)
    browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')

    # THEN
    browser.assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=8))

    browser.quit()