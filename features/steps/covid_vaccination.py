from behave import given, when, then
from vaccine import CovidVaccine


covid_vaccine = CovidVaccine(age=55)


@given('a user with age above 55')
def step_impl(context):
    assert (covid_vaccine.is_elder() is True)


@when('the user is moved to express counter')
def step_impl(context):
    assert (covid_vaccine.fast_track_user() == 'user issued fast-track pass')


@then('the user received vaccine shot')
def step_impl(context):
    assert (covid_vaccine.administer_shot() == 'Administering COVID vaccine')
