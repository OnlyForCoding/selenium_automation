import pytest
import utilities.custom_logger as cl
import logging
from selenium import webdriver


@pytest.yield_fixture()
def set_up():
    log = cl.customLogger(logging.DEBUG)
    log.info("Running method level setUp")
    yield
    log.info("Running method level tear down")


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    log = cl.customLogger(logging.DEBUG)
    log.info("Running one time setUp")
    if browser == 'chrome':
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path="C:/Users/MCPL#L92/Downloads/chromedriver_win32/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.delete_all_cookies()
        driver.get(baseURL)
        log.info("Running test on Firefox")
    else:
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path="C:/Users/MCPL#L92/Downloads/chromedriver_win32/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        log.info("Running test on Chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    log.info("Running one time tear down")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")
