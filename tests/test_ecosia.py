from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from webdriverproject.conditions import type, click, number_of_elements, assert_that, browser_open

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


browser_open('https://ecosia.org')
# wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))  # явное ожидание

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

query = '[name=q]'

# query = type_to_element('[name=q]')
# query.type('selene yashaka pulls' + Keys.ENTER))
# type_to_element('[name=q]').type('selene yashaka pulls' + Keys.ENTER))

# type_to_element('[name=q]', value='selene yashaka pulls' + Keys.ENTER)
type(query, value='selene yashaka pulls' + Keys.ENTER)

# click_on_element('[data-test-id=mainline-result-web]:nth-of-type(1) a')
click('[data-test-id=mainline-result-web]:nth-of-type(1) a')

click('#pull-requests-tab')

# assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=8)
assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=8))

'''
Basic Webrdiver (unstable): 
number_of_pulls = len(driver.find_elements(By.CSS_SELECTOR, '[id^=issue_]:not([id$=_link])'))
assert number_of_pulls == 8
'''


