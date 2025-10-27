from behave import given, when, then
from selenium import webdriver
from pages.lastfm_home_page import LastfmHomePage
from pages.lastfm_results_page import ResultsPage
from pages.lastfm_artist_page import ArtistPage

@given('el usuario esta en el home page de last.fm')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.last.fm/")
    context.lastfm_home = LastfmHomePage(context.driver)

@when('el usuario busca el artista "{artist_name}"')
def step_search_artist(context, artist_name):
    context.lastfm_home.search_artist(artist_name)
    context.lastfm_results = ResultsPage(context.driver)

#para el and usamos when

@when("selecciona el primer resultado de la busqueda")
def step_select_result(context):
    context.lastfm_results.click_artist_name()
    context.artist_page = ArtistPage(context.driver)

@then('la fecha del ultimo release debe ser "{last_release_date}"')
def step_check_last_release_date(context, last_release_date):
    obtained_date = context.artist_page.get_last_release_date()
    assert obtained_date == last_release_date, f"La fecha del ultimo release no coincide"
