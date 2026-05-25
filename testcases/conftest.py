import pytest
from selenium import webdriver

@pytest.fixture()
def setup():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practice.qabrains.com/")
    driver.implicitly_wait(5)

    yield driver
    driver.quit()



@pytest.fixture(params=[ ("qa_testers@qabrains.com","Password123","Pass"),
                         ("qa_testers@qabrains.com1","Password123","Fail"),
                         ("qa_testers@qabrains.com","Password1231","Fail"),
                         ("qa_testers@qabrains.com1","Password1231","Fail")])

def dataForlogin(request):
    return request.param



