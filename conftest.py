import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Обработчик командной строки, который считывает из командной строки параметр language
#Тест должен запускаться с параметром language например командой: pytest --language=es test_items.py

#Регистрируем опцию language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

#Получаем значение опции language
@pytest.fixture()
def language(request):
    """Фикстура, возвращающая выбранный язык"""
    return request.config.getoption('--language')

#Логика запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.


#Запускаем браузер с языком
@pytest.fixture()
def browser(language):
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

