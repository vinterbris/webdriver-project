from selenium.webdriver.chrome.webdriver import WebDriver

from webdriverproject.selector import to_locator


def number_of_elements(selector, value: int):
    def assertion(driver: WebDriver):
        webelements = driver.find_elements(*to_locator(selector))
        actual_value = len(webelements)
        if actual_value != value:
            raise AssertionError(f'Number of elements is not {value}\nActual value = {actual_value}')
        else:
            return webelements

    return assertion
