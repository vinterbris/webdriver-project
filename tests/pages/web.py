from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from tests.pages.ecosia import Ecosia
from tests.pages.github import Issues
from webdriverproject.browser import Browser, Config

browser = Browser(
    webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
    Config(timeout=3, base_url='https://ecosia.org')
)

ecosia = Ecosia(browser)
github_issues = Issues(browser)