from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Click:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.click_button_id = "//*[@id = 'badButton']"
        self.click_button_class = "//*[contains(@class,'btn-success')]"

    def load_click_page(self, base_url):
        url = f"{base_url}/click"
        self.browser.get(url)

    def click_on_button(self):
        self.browser.find_element(By.XPATH, self.click_button_id).click()

    def verify_button_click(self):
        self.browser.find_element(By.XPATH, self.click_button_class)
