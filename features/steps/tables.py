import time

from behave import *
from features.environment import *


@given('the simple table')
def step_impl(context):
    context.browser.get("https://practice-automation.com/tables/")


@when('I extract data from the table')
def step_impl(context):
    simple_table = context.browser.find_element(By.TAG_NAME, "tbody")
    print(simple_table.text)


@then('the values will be available for analysis')
def step_impl(context):
    print("Values from the table are printed to terminal.")
    pass


@given('the search input field')
def step_impl(context):
    context.browser.get("https://practice-automation.com/tables/")
    context.search_input = context.browser.find_element(By.CSS_SELECTOR, "input[aria-controls='tablepress-1']")


@when('I type {search_term}')
def step_impl(context, search_term):
    context.search_term = search_term
    context.search_input.send_keys(search_term)

    time.sleep(2)


@then('the table should show only the row of interest')
def step_impl(context):
    time.sleep(2)
    rows = context.browser.find_elements(By.XPATH, "//table[@id='tablepress-1']/tbody/tr")

    assert len(rows) == 1, f"Expected 1 row in the table after filtering, but found {len(rows)}."
