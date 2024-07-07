from selenium.webdriver import Keys

from webdriverproject.browser import Browser, number_of_elements

browser = Browser()

browser.open('https://ecosia.org')

query = '[name=q]'

# WHEN
browser.type(query, value='selene yashaka pulls' + Keys.ENTER)
browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')

# THEN
browser.assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=8))
