from dataclasses import dataclass

from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

from webdriverproject.selector import to_locator
from webdriverproject.wait import WebDriverWait


@dataclass
class Config:
    timeout: float = 2
    base_url:str = ''


class Browser:
    def __init__(self, driver: WebDriver, config=Config()):
        self.driver = driver
        self.config = config
        self.wait = WebDriverWait(self.driver, timeout=config.timeout, ignored_exceptions=(WebDriverException,))

    def open(self, relative_url):
        self.driver.get(self.config.base_url + relative_url)

    def _element(self, selector):
        def command(driver: WebDriver):
            webelement = driver.find_element(*to_locator(selector))
            if not webelement.is_displayed():
                raise AssertionError(f'element is not displayed: {webelement.get_attribute('outerHTML')}')
            return webelement

        return self.wait.until(command)

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
