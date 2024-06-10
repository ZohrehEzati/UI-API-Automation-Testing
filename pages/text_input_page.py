from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TextInput:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.text_input_id = "//*[@id = 'newButtonName']"
        self.button_id = "//*[@id = 'updatingButton']"

    def load_text_input_page(self, base_url):
        url = f"{base_url}/textinput"
        self.browser.get(url)

    def enter_text_to_input(self, new_name):
        self.browser.find_element(By.XPATH , self.text_input_id).send_keys(new_name)

    def press_the_button(self):
        self.browser.find_element(By.XPATH, self.button_id).click()

    def verify_changed_button_name(self, new_name):
        button_text = self.browser.find_element(By.XPATH, self.button_id).text
        assert button_text == new_name


