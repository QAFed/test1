import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure


@pytest.fixture(scope="session")
def t_browser(request):
    with allure.step("Получен экземпляр браузера"):
        service= Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        request.addfinalizer(driver.quit)
        return driver