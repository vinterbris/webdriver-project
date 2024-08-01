from selenium.webdriver import Keys

from tests.pages import github, ecosia, web
from tests.pages.web import browser


def test_number_of_pull_requests():
    browser.open('/')

    # WHEN
    web.ecosia.query.type('selene yashaka pull requests' + Keys.ENTER)
    web.ecosia.first_result_link.click()

    # THEN
    web.github_issues.links.should_have_size(9)

    browser.quit()
