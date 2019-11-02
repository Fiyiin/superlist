import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())


    def tearDoown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-do', self.browser.title)
        self.fail('Flush the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')