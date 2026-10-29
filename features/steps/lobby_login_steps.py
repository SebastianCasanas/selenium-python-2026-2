from behave import given, when, then
from pages.lobby_login_page import LobbyLoginPage
from pages.lobby_dashboard_page import LobbyDashboardPage


@given('El usuario se encuentra en la página de login')
def step_given_user_on_login_page(context):
    context.lobby_login_page = LobbyLoginPage(context.driver)
    context.lobby_login_page.open()


@when('El usuario ingresa con el nombre "{username}"')
def step_when_user_logs_in(context, username):
    context.lobby_login_page.login(username)
    context.lobby_dashboard_page = LobbyDashboardPage(context.driver)


@then('El nombre del usuario "{username}" aparece en el dashboard')
def step_then_user_login(context, username):
    assert context.lobby_dashboard_page.find_username(username) is True


@then('Se muestra un mensaje de error')
def step_then_error_message(context):
    assert context.lobby_login_page.is_error_displayed()
    assert context.lobby_login_page.get_error_message() != ""
    assert context.lobby_login_page.is_still_on_login_page()
