import chromedriver_binary
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='function')
def browser():
    print('\nstart test')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit test')
    browser.quit()