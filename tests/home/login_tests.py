from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

   def test_validLogin(self):
       baseURL = "https://letskodeit.teachable.com/"
       driver = webdriver.Chrome(executable_path="C:/Users/MCPL#L92/Downloads/chromedriver_win32/chromedriver.exe")
       driver.maximize_window()
       driver.implicitly_wait(3)
       driver.get(baseURL)
       lp = LoginPage(driver)
       lp.login("test@email.com","abcabc")

