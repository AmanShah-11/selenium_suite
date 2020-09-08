import unittest
from HTMLTestRunner import HTMLTestRunner
import os
from test_file2 import SearchText
from test_file3 import HomePageTest

# get the directory path to output report file
dir = os.getcwd()  # os.getcwd gets the current directory

# Get all test from SearchTet and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Create a test suite combining search_Text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# Open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")
# Configure HTMlTestRunner options
runner = HTMLTestRunner(stream=outfile, title='Test Report', description= "Acceptance Tests")

# run the suite using HTMlTestRunner
runner.run(test_suite)



