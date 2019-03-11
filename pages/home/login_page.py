from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def click_login_link(self):
        self.element_click(self._login_link, locator_type="link")

    def enter_email(self, email):
        self.send_my_keys(self._email_field, email)

    def enter_password(self, password):
        self.send_my_keys(self._password_field, password)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="name")

    def login(self, email, password):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

