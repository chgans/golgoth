from selenium import webdriver

def before_all(context):
    # /usr/local/bin/phantomjs
    # context.browser = webdriver.Firefox()
    # context.browser.implicitly_wait(2)
    context.browser = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    context.browser.set_window_size(1280, 1024)
    context.browser.implicitly_wait(2)
    context.server_url = 'https://localhost:8000'

def after_all(context):
    context.browser.quit()

def before_feature(context, feature):
    pass
