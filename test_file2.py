# Please work
import unittest
from selenium import webdriver
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

    def test_search_by_test(self):
        # Get the search textbox
        self.search_field = self.driver.find_element_by_name("q")

        # Enter search keyword and submit
        self.search_field.clear()
        self.search_field.send_keys("Selenium WebDriver Interview question")
        self.search_field.submit()

        # Get the list of elements which are displayed after the search has been done
        self.driver.implicitly_wait(LOAD_TIME)
        list = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "r")))
        lists = self.driver.find_elements_by_class_name("r")
        self.assertEqual(10, len(lists))

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        # enter serach keyword and submit
        self.search_field.clear()
        self.search_field.send_keys("Python Class")
        self.search_field.submit()
        # get the list of elements which are displayed after the search
        # Currently on result page using find_elements_by_class_name method
        list_new = self.driver.find_elements_by_class_name("r")
        self.assertEqual(10, len(list_new))

    @classmethod
    def tearDownClass(cls):
        # Closes the browser window
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()







