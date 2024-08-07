from __future__ import annotations

from dataclasses import dataclass

from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

from webdriverproject.conditions import have
from webdriverproject.selector import to_locator
from webdriverproject.wait import WebDriverWait


@dataclass
class Config:
    timeout: float = 2
    base_url: str = ''


class Element:
    def __init__(self, selector, browser: Browser):
        self.selector = selector
        self.browser = browser

    def type(self, value):
        self.browser.type(self.selector, value)
        return self

    def click(self):
        self.browser.click(self.selector)
        return self


class Collection:
    def __init__(self, selector, browser: Browser):
        self.selector = selector
        self.browser = browser

    def should_have_size(self, value):
        self.browser.should(have.number_of_elements(self.selector, value=value))


class Browser:
    def __init__(self, driver: WebDriver, config=Config()):
        self.driver = driver
        self.config = config
        self.wait = WebDriverWait(self.driver, timeout=config.timeout, ignored_exceptions=(WebDriverException,))

    def open(self, relative_url):
        self.driver.get(self.config.base_url + relative_url)

    def type(self, selector, value):
        def command(driver: WebDriver):
            webelement = driver.find_element(*to_locator(selector))
            webelement.send_keys(value)
            return webelement

        return self.wait.until(command, message=f'failed to type "{value}" into element by {selector}')

    def click(self, selector):
        def find_element_and_click(driver: WebDriver):
            driver.find_element(*to_locator(selector)).click()
            return True

        return self.wait.until(find_element_and_click, message=f'failed to click on element {selector}')

    def should(self, condition):
        return self.wait.until(condition)

    def quit(self):
        self.driver.quit()

    def element(self, selector) -> Element:
        return Element(selector, self)

    def all(self, selector) -> Collection:
        return Collection(selector, self)
