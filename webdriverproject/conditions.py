from typing import Tuple

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _element_if_visible
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))

def browser_open(url):
    driver.get(url)

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


def type(selector, value):
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        webelement.send_keys(value)
        return webelement

    wait.until(command)


def click(selector):
    def find_element_and_click(driver: WebDriver):
        driver.find_element(*to_locator(selector)).click()
        return True

    wait.until(find_element_and_click)

def number_of_elements(selector, value: int):
    def predicate(driver: WebDriver):
        webelements = driver.find_elements(*to_locator(selector))
        return len(webelements) == value

    return predicate

def assert_that(elements):
    wait.until(elements)