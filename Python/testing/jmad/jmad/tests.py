from django.test import LiveServerTestCase
from selenium import webdriver

class DTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        # self.browser.implicitly_wait(2)

    def test_1(self):
        page = self.browser.get(self.live_server_url + '/')
        self.fail('fail')

    def tearDown(self):
        pass
        # self.browser.quit()

