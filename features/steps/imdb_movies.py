from behave import given, when, then
from selenium import webdriver
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_results_page import ImdbResultsPage
from pages.imdb_movie_page import ImdbMoviePage


@given('el usuario esta en el home page de imdb')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.imdb_home = ImdbHomePage(context.driver)

@when('el usuario busca la película "{movie_name}"')
def step_search_movie(context, movie_name):
    context.imdb_home.search_movie(movie_name)
    context.results_page = ImdbResultsPage(context.driver)

@when('el usuario selecciona el primer resultado de la busqueda')
def step_select_result(context):
    context.results_page.click_movie_name()
    context.imdb_movie = ImdbMoviePage(context.driver)

@then('el nombre de la película debe ser "{movie_name}"')
def step_validate_movie_name(context, movie_name):
    assert context.imdb_movie.get_movie_title() == movie_name, \
        f"El nombre de la película no coincide, se esperaba {movie_name} y se obtuvo {context.imdb_movie.get_movie_title()} "

@then('el rating de la película debe ser "{movie_rating}"')
def step_validate_movie_rating(context, movie_rating):
    assert context.imdb_movie.get_movie_rating() == movie_rating,\
        f"El rating de la película no coincide, se esperaba {movie_rating} y se obtuvo {context.imdb_movie.get_movie_rating()}"

