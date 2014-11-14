from behave import given, when, then, step
from search.management.commands.create_session import create_pre_authenticated_session
from django.conf import settings


@given('I am a logged-in user')
def given_i_am_logged_in(context):
    session_key = create_pre_authenticated_session(email='a@b.c')
    ## to set a cookie we need to first visit the domain.
    ## 404 pages load the quickest!
    url = context.server_url + "/admin/login/?next=/admin/"
    url = 'http://google.com'
    context.browser.get(url)
    print(url, context.browser.current_url)
    context.browser.add_cookie(dict(
        name=settings.SESSION_COOKIE_NAME,
        value=session_key,
        path='/',
    ))

@when('I create a dork {dork_name} with "{dork_content}"')
def create_a_dork(context, dork_name, dork_content):
    context.browser.get(context.server_url)
    context.browser.find_element_by_id('id_dork_name').send_keys(dork_name)
    context.browser.find_element_by_id('id_dork_content').send_keys('\n')
    context.browser.find_element_by_id('id_dork_submit').click()

@when('I click the link to "{link_text}"')
def click_a_link(context, link_text):
    assert False

@then('I will see the dork content "{dork_content}"')
def see_a_dork(context, dork_content):
    assert False

@then('I will see a link to "{link_text}"')
def see_a_link(context, link_text):
    assert False

@then('I will see the dork name "{dork_name}"')
def see_a_dork_name(context, dork_name):
    assert False
