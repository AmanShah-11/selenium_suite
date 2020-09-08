# Please work
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Global variables
PATH = "C:\Program Files (x86)\chromedriver.exe"
LOAD_TIME = 10


class SearchText(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Precquisities before each test case
        cls.driver = webdriver.Chrome(PATH)
        cls.driver.implicitly_wait(LOAD_TIME)
        cls.driver.maximize_window()
        cls.driver.get("https://www.google.com/")

    def test_search_box(self):
        # Check serach box exists on Home page
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_language_settings(self):
        # Check language options on Home page
        self.assertTrue(self.is_element_present(By.ID, "_eEe"))

    def test_images_link(self):
        # Check images link on Home page
        images_link = self.driver.find_element_by_link_text("Images")
        images_link.click()
        # Check search field exists on Image page
        self.assertTrue(self.is_element_present(By.NAME, "q"))
        self.search_field = self.driver.find_element_by_name("q")
        # Enter serach keyword and submit
        self.search_field.send_keys("Selenium Webdriver framework architecture diagram")
        self.search_field.submit()

    @classmethod
    def tearDownClass(cls):
        # Closes the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        '''
        Helper method to confirm the presence of an element on page
        :param how: By locator type
        :param what: Locator valye
        :return: True
        '''
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

if __name__ == "__main__":
    unittest.main(verbosity=2)







