from behave import *


from features.environment import *


@given('the calendar')
def step_impl(context):
    context.browser.get("https://practice-automation.com/calendars/")


@when('I select the date')
def step_impl(context):
    context.browser.find_element(By.ID, "g1065-selectorenteradate").send_keys('2021-01-15')
    context.browser.find_element(By.ID, "g1065-selectorenteradate").send_keys(keys.Keys.RETURN)

    context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

@then('I should be able to see selected date on the next page')
def step_impl(context):
    date = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "field-value"))).get_attribute("innerHTML")

    assert date == "2021-01-15", f"Expected 'January 15, 2021', got '{date}' instead"