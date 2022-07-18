from features.browser import Browser
import os
import datetime


def before_all(context):
    context.executionFolder = 'evidences/execution' + str(datetime.datetime.now())[0:19].replace(':', '.') + '/'


def before_tag(context, tag):
    if tag == "web":
        context.browser = Browser("chrome")
        context.driver = context.browser.getDriver()
        context.scenarioFolder = context.executionFolder + context.scenario.name
        os.makedirs(context.scenarioFolder)


def after_tag(context, tag):
    if tag == "web":
        context.browser.close()
        context.browser.quit()
