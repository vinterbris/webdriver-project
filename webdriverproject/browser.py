from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _element_if_visible

from webdriverproject.selector import to_locator
from webdriverproject.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, timeout=2, ignored_exceptions=(WebDriverException,))

    def open(self, url):
        self.driver.get(url)

    def element(self, selector):
        def command(driver):
            return _element_if_visible(driver.find_element(*to_locator(selector)))

        return self.wait.until(command)

    def type(self, selector, value):
        def command(driver: WebDriver):
            webelement = driver.find_element(*to_locator(selector))
            webelement.send_keys(value)
            return webelement

        return self.wait.until(command)

    def click(self, selector):
        def find_element_and_click(driver: WebDriver):
            driver.find_element(*to_locator(selector)).click()
            return True

        return self.wait.until(find_element_and_click)

    # def assert_number_of_elements(self, selector, value: int):
    #     def assertion(driver: WebDriver):
    #         webelements = driver.find_elements(*to_locator(selector))
    #         actual_value = len(webelements)
    #         if actual_value != value:
    #             raise AssertionError(f'Number of elements is not {value}\nActual value = {actual_value}')
    #
    #     return self.wait.until(assertion)

    def assert_that(self, condition):
        return self.wait.until(condition)

    def quit(self):
        self.driver.quit()



