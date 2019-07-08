# this is a test file to run test on the app file

import unittest
from app import addTwoNumbers

class TestAppMethods(unittest.TestCase):
	def test_add_two_numbers(self):
		self.assertEqual(addTwoNumbers(2,3), 5)

if __name__ == '__main__':
	unittest.main()
