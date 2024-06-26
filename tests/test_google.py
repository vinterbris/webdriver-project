from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from webdriverproject.conditions import type_to_element, click_on_element, number_of_elements

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# selene: browser.open()
driver.get('https://ecosia.org')
wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))  # явное ожидание
driver.implicitly_wait(2)  # неявное ожидание // по большей части бесполезные, нужны только в очень узких ситуациях

'''
In Selene:
browser.element('[name=q]').type('selene).press_enter()

In Selenium Webdriver:  
driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene', Keys.ENTER)

Or with waits:
def find_element(driver):
    return driver.find_element(By.CSS_SELECTOR, '[name=q]')
wait.until(find_element).send_keys('selene', Keys.ENTER)

Same with lambda:
wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '[name=q]')).send_keys('selene yashaka', Keys.ENTER)
click
wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '[data-test-id=mainline-result-web]:nth-of-type(1) a')).click()

Webdriver expected condition:
 wait.until(visibility_of_element_located((By.NAME, 'q'))).send_keys('selene yashaka', Keys.ENTER)
 
With custom expected condition:
wait.until(element('[name=q]')).send_keys('selene yashaka', Keys.ENTER)
wait.until(element('[data-test-id=mainline-result-web]:nth-of-type(1) a')).click()
'''

# type_to_element('[name=q]', value='selene yashaka pulls' + Keys.ENTER)
wait.until(type_to_element('[name=q]', value='selene yashaka pulls' + Keys.ENTER))

# click_on_element('[data-test-id=mainline-result-web]:nth-of-type(1) a')
wait.until(click_on_element('[data-test-id=mainline-result-web]:nth-of-type(1) a'))

wait.until(click_on_element('#pull-requests-tab'))



# assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=8)
wait.until(number_of_elements('[id^=issue_]:not([id$=_link])', value=8))
'''
Basic Webrdiver (unstable): 
number_of_pulls = len(driver.find_elements(By.CSS_SELECTOR, '[id^=issue_]:not([id$=_link])'))
assert number_of_pulls == 8
'''