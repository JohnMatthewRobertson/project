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

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(StaticLiveServerTestCase):
    """ base setup for gettting webbrowser and tear down"""

    def setUp(self):
        ''' get browser driver automatically '''
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        self.correct_test_username = 'testuserone'
        self.correct_test_userpassword = 'testpass123'
        self.correct_test_useremail = 'testuserone@email.com'

        self.wrong_test_username = 'testwronguser'
        self.wrong_test_userpassword = 'testpwrongpassword'
        self.wrong_test_useremail = 'testwrongemail@email.com'

    def tearDown(self):
        self.browser.close()
