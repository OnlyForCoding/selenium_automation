from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_set_up(self, one_time_setup):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        assert self.lp.verify_successful_login() == True

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("test@email.com", "euwhrwurh")
        assert self.lp.verify_login_failed() == True
