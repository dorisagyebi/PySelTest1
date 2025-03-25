from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class SignInPage:
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='http://courses.ultimateqa.com/users/sign_in']")
    SIGNIN_URL = "https://courses.ultimateqa.com/users/sign_in"
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[id='user[email]']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[id='user[password]']")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, "input[id='user[remember_me]']")
    SIGNIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
   
   
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click_login_link(self):
        login_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_LINK))
        login_link.click()

    def verify_signin_page(self):
        """Verify the current URL is the signin page."""
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.SIGNIN_URL))
        assert self.driver.current_url == self.SIGNIN_URL, (
            f"Expected URL: {self.SIGNIN_URL}, but got: {self.driver.current_url}"
        )

    def fill_email(self, email):
        """Fill in the email field."""
        self.enter_text(self.EMAIL_FIELD, email)

    def fill_password(self, password):
        """Fill in the password field."""
        self.enter_text(self.PASSWORD_FIELD, password)

    def toggle_checkbox(self):
        """Toggle the 'Remember Me' checkbox using ActionChains."""
        element = self.wait.until(EC.element_to_be_clickable(self.REMEMBER_ME_CHECKBOX))
        ActionChains(self.driver).double_click(element).perform()

    def click_signin_btn(self):
        """Click the sign-in button."""
        self.click_element(self.SIGNIN_BTN)

    def complete_login(self, email, password):
        """Perform the complete login process."""
        self.fill_email(email)
        self.fill_password(password)
        self.toggle_checkbox()
        self.click_signin_btn()
