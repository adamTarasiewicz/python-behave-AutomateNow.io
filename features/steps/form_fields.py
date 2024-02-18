from behave import *

from features.environment import *
from selenium.webdriver.common.alert import Alert


@given('the form')
def step_impl(context):
    context.browser.get("https://practice-automation.com/form-fields/")


@when('I fill the form and click submit')
def step_impl(context):
    try:
        context.browser.find_element(By.ID, "cookie_action_close_header").click()
    except NoSuchElementException:
        pass
    context.browser.find_element(By.ID, "name").send_keys("Adam")
    context.browser.find_element(By.CSS_SELECTOR, "input[value='Coffee']").click()
    context.browser.find_element(By.XPATH, "//input[@value='Yellow']").click()

    dropdown = context.browser.find_element(By.ID, "siblings")
    select = Select(dropdown)
    select.select_by_value("no")
    # or select.select_by_visible_text("No")

    context.browser.find_element(By.ID, "email").send_keys('google@google.com')
    context.browser.find_element(By.ID, "message").send_keys('My test message')

    submit_btn = context.browser.find_element(By.ID, "submit-btn")
    context.browser.execute_script("arguments[0].click();", submit_btn)


@then('I should see message sent confirmation')
def step_impl(context):
    alert = Alert(context.browser)
    alert_text = alert.text

    assert alert_text == "Message received!", f"Expected: 'Message received!' got '{alert_text}' instead"
