import pytest
from selenium import webdriver
from pages.signin_page import SignInPage


@pytest.fixture
def setup():
    """Setup the WebDriver for the test."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://ultimateqa.com/automation")
    yield driver
    driver.quit()


def test_signin(setup):
    signin_page = SignInPage(setup)

    # Navigate to sign-in page
    signin_page.click_login_link()

    # Verify sign-in page is displayed
    signin_page.verify_signin_page()
    
    # Perform login process
    signin_page.complete_login(email="nanagyebi@gmail.com", password="N@ruTO")
    
