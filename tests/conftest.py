import pytest
from selenium import webdriver
from base.wedriverfactory import WebdriverFactory

@pytest.yield_fixture()  # concept of fixture in pytest to make one call before  # we can use fixture which supports
def Set():
    print("called conftest py")
    print("\n once before evry method")
    yield
    print("  once after every method")


@pytest.yield_fixture(scope="class")  # concept of fixture in pytest to make one call before  # we can use fixture which supports class for class
def onetimeSet(request,browser):
    print("only one during test-start")
    wdf = WebdriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("only one during test-end")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="type of os")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--osType")
