'''
    start a selenium webdrive that will open firefox browser
    assert that the web page has 'Django' in its title
    functional tests test the application from the outside,
    from the point of view of the user.
    Unit tests test the application from the inside,
    from the point of view of the programmer.
    The functional tests are the ultimate judge of
    whether your application works or not.
    The unit tests are a tool to help you along the way.
    terminology:
        Functional test,
        acceptance test,
        end to end test,
        behavioral test
        isolated test,
        integrated test,
        unittest
    to run the functional test
        python -m unittest -v functionalTest.py
    To run in headless mode not opening the browser
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.add_argument("--headless")
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from webdriver_manager.firefox import GeckoDriverManager
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        ''' get browser driver automatically '''
        self.MAX_WAIT = 10
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def tearDown(self):
        self.browser.refresh()
        self.browser.close()
