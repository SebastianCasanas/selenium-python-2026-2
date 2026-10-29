import time
from behave import given, when, then
from pages.lobby_login_page import LobbyLoginPage
from pages.lobby_dashboard_page import LobbyDashboardPage


@given('the user is on the lobby page')
def step_open_lobby(context):
    context.lobby_login_page = LobbyLoginPage(context.driver)
    context.lobby_login_page.open()


@when('the user joins with a unique name')
def step_join_unique_name(context):
    context.username = f"sebas{int(time.time())}"
    context.lobby_login_page.join(context.username)


@when('the user joins with the name "{name}"')
def step_join_with_name(context, name):
    context.lobby_login_page.join(name)


@then('the user should see their name in the lobby')
def step_name_in_lobby(context):
    dashboard = LobbyDashboardPage(context.driver)
    assert dashboard.is_user_in_lobby(context.username)


@then('a name error message should be displayed')
def step_name_error(context):
    assert context.lobby_login_page.is_error_displayed()
    assert context.lobby_login_page.get_error_message() != ""
    assert context.lobby_login_page.is_still_on_login_page()
