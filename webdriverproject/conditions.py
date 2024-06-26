from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _element_if_visible


def to_locator(selector: str) -> Tuple[str, str]:
    return (By.XPATH, selector) if (
            selector.startswith('/')
            or selector.startswith('//')
            or selector.startswith('./')
            or selector.startswith('..')
            or selector.startswith('(')
    ) else (By.CSS_SELECTOR, selector)


def element(selector):
    def find_visible_element(driver):
        return _element_if_visible(driver.find_element(*to_locator(selector)))

    return find_visible_element


def type_to_element(selector, value):
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        webelement.send_keys(value)
        return webelement

    return command


def click_on_element(selector):
    def find_element_and_click(driver: WebDriver):
        driver.find_element(*to_locator(selector)).click()
        return True

    return find_element_and_click


def number_of_elements(selector, value: int):
    def predicate(driver: WebDriver):
        webelements = driver.find_elements(*to_locator(selector))
        return len(webelements) == value

    return predicate


'''
BEFORE:
def number_of_elements(selector, value: int):
    selector_type = By.XPATH if (
            selector.startswith('/')
            or selector.startswith('//')
            or selector.startswith('./')
            or selector.startswith('..')
            or selector.startswith('(')
    ) else By.CSS_SELECTOR

    def predicate(driver: WebDriver):
        webelements = driver.find_elements(selector_type, selector)
        return len(webelements) == value

    return predicate
'''
