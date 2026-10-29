from behave import given, when, then
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_results_page import ImdbResultsPage
from pages.imdb_movie_page import ImdbMoviePage


@given('the user is on the IMDb home page')
def step_open_imdb(context):
    context.imdb_home_page = ImdbHomePage(context.driver)
    context.imdb_home_page.open()


@when('the user searches for the movie "{movie}"')
def step_search_movie(context, movie):
    context.imdb_home_page.search(movie)


@when('the user opens the first result')
def step_open_first_result(context):
    ImdbResultsPage(context.driver).open_first_result()


@then('the movie rating should be displayed')
def step_rating_displayed(context):
    rating = ImdbMoviePage(context.driver).get_rating()
    print(f"Rating: {rating}")
    value = float(rating.replace(",", "."))
    assert 0 < value <= 10
