import unittest
from test_file2 import SearchText
from test_file3 import HomePageTest

# get all tests from SearchText and HomepageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# Run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)