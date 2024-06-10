import pytest
from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from pages.click_page import Click
from pages.text_input_page import TextInput
from time import sleep
from selenium.webdriver.chrome.options import Options


BASE_URL = 'http://www.uitestingplayground.com'


@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--enable-logging')
    options.add_argument('--v=1')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    # Tear Down
    driver.quit()


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def click(browser):
    return Click(browser)


@pytest.fixture
def text_input(browser):
    return TextInput(browser)


# Start ---- Scenario: Verify Button Click
@given(parsers.cfparse('I navigate to the click page'))
def navigate_to_click_page(click, base_url):
    click.load_click_page(base_url)


@when(parsers.cfparse('I click the button'))
def click_the_button(click):
    click.click_on_button()


@then(parsers.cfparse('the button class should change to "btn-success"'))
def verify_click(click):
    click.verify_button_click()


# The End ---- Scenario: Verify Button Click


# Start ---- Scenario: Verify Text Input

@given(parsers.cfparse('I navigate to the text input page'))
def navigate_to_text_input_page(text_input, base_url):
    text_input.load_text_input_page(base_url)


@when(parsers.cfparse('I set the text "{new_name}" into the input field'))
def set_text(text_input, new_name):
    text_input.enter_text_to_input(new_name)


@when(parsers.cfparse('I press the button'))
def press_button_text(text_input):
    text_input.press_the_button()


@then(parsers.cfparse('the button text should be changed to "{new_name}"'))
def verify_button_text(text_input, new_name):
    text_input.verify_changed_button_name(new_name)

# The End ---- Scenario: Verify Text Input


@scenario('../features/test_ui.feature', 'Verify Button Click')
def test_verify_button_click():
    pass


@scenario('../features/test_ui.feature', 'Verify Text Input')
def test_verify_text_input():
    pass
