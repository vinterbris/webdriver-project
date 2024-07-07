from typing import Tuple

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _element_if_visible
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, timeout=2, ignored_exceptions=(WebDriverException,))

    def open(self, url):
        self.driver.get(url)

    def element(self, selector):
        def find_visible_element(driver):
            return _element_if_visible(driver.find_element(*to_locator(selector)))

        return find_visible_element

    def type(self, selector, value):
        def command(driver: WebDriver):
            webelement = driver.find_element(*to_locator(selector))
            webelement.send_keys(value)
            return webelement

        self.wait.until(command)

    def click(self, selector):
        def find_element_and_click(driver: WebDriver):
            driver.find_element(*to_locator(selector)).click()
            return True

        self.wait.until(find_element_and_click)

    def assert_that(self, elements):
        self.wait.until(elements)

    def quit(self):
        self.driver.quit()


def to_locator(selector: str) -> Tuple[str, str]:
    return (By.XPATH, selector) if (
            selector.startswith('/')
            or selector.startswith('//')
            or selector.startswith('./')
            or selector.startswith('..')
            or selector.startswith('(')
    ) else (By.CSS_SELECTOR, selector)


def number_of_elements(selector, value: int):
    def predicate(driver: WebDriver):
        webelements = driver.find_elements(*to_locator(selector))
        return len(webelements) == value

    return predicate
