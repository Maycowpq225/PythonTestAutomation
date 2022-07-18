from features.browser import Browser

def before_all(context):
    print("TESTEEEEEEEEEEEEEEEEEEEE")

def before_tag(context, tag):
    if tag == "web":
        context.browser = Browser("chrome")
        context.driver = context.browser.getDriver()


def after_tag(context, tag):
    if tag == "web":
        context.browser.close()
        context.browser.quit()
