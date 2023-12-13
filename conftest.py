import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language for the browser')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
# 'intl.accept_languages' устанавливает предпочтительный язык для отображения веб-страниц.
# В данном коде значение этого параметра устанавливается в значение переменной user_language, которое берется из командной строки при запуске теста
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
