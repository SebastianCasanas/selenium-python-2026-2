from behave import given, when, then
from pages.lobby_login_page import LobbyLoginPage
from pages.lobby_dashboard_page import LobbyDashboardPage


@given('El usuario se encuentra en la página de login')
def step_given_user_on_login_page(context):
    context.lobby_login_page = LobbyLoginPage(context.driver)
    context.lobby_login_page.open()


@when('El usuario ingresa con el nombre "{username}"')
def step_when_user_enters_name(context, username):
    context.lobby_login_page.join(username)


@then('El nombre del usuario "{username}" aparece en el dashboard')
def step_then_username_in_dashboard(context, username):
    dashboard = LobbyDashboardPage(context.driver)
    assert dashboard.find_username(username)


@then('Se muestra un mensaje de error')
def step_then_error_message(context):
    assert context.lobby_login_page.is_error_displayed()
    assert context.lobby_login_page.get_error_message() != ""
    assert context.lobby_login_page.is_still_on_login_page()
