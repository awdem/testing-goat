import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # User goes to check out homepage
        self.browser.get("http://localhost:8000")
        # User sees page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)

        # User is invited to enter a to-do item straight away
        self.fail("Finish the test!")
        # User types "Buy peacock feathers" into a text box

        # When User hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # User enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on their list

if __name__ == "__main__":
    unittest.main()
