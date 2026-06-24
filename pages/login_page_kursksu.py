from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://my.kursksu.ru"
        
        # Инкапсулируем все локаторы в одном месте
        self.login_input = page.locator("input[type='text'], input[type='email']").first
        self.password_input = page.locator("input[type='password']").first
        self.submit_button = page.locator("button", has_text="Войти")
        self.error_message = page.locator(".alert-danger")

    # Метод для открытия страницы
    def open(self):
        self.page.goto(self.url)

    # Универсальный метод для авторизации
    def login(self, username, password):
        self.login_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()