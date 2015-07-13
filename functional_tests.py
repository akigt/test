# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):	
		#Edith has heard about a cool new online to-do.app
		#she goes to check out its homepage
		self.browser.get('http://localhost:8000')

		#she notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		#she is invited to enter a to-do item straight away
		
		#She types "Buy peacock feathers" into a text box (Edith'S hobby is
		#tying fly-fishing lures)
		
		#When she hits enter, the page updates, and now the page lists
		#"1: Buy peacock feathers" as a n item in a to-dp list
		
		#There is still a text box inviting her to add another item.
		#She enters "Use peacok feathers to make a fly" (Edith is very methodical)
		
		#the page updatees again, and now shows both items on her list
		#Edith wonders wether the site will remember her list.
		#Then she sees that the site has generated a unique URL for her --
		#there is some explanatory text to that effect.
		
		#She visits that URL -her to-do- list is still here
		
		#Satisfied, she goes back to sleep
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')