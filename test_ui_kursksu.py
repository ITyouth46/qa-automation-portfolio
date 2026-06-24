import pytest
from playwright.sync_api import Page
from pages.login_page_kursksu import LoginPage # Импортируем наш новый класс

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "slow_mo": 1500,
    }

@pytest.mark.skip(reason="Сайт КГУ блокирует запросы с IP-адресов GitHub (США)")
def test_kgu_failed_login(page: Page):
    # Инициализируем страницу
    login_page = LoginPage(page)
    
    # Сценарий читается как обычный английский текст:
    login_page.open()
    login_page.login("aboba_test_user", "wrong_password")
    
    # Тест занимается только проверками (assert)
    assert login_page.error_message.is_visible()

@pytest.mark.skip(reason="Сайт КГУ блокирует запросы с IP-адресов GitHub (США)")
def test_kgu_empty_login(page: Page):
    login_page = LoginPage(page)
    
    login_page.open()
    login_page.login("", "")
    
    assert "login" in page.url
    assert not login_page.error_message.is_visible()