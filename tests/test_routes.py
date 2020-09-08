from flask import Flask
import json
from appl import app
import unittest

class FlaskTest(unittest.TestCase):
	def test_index(self):
		tester=app.test_client(self)
		response=tester.get("/")
		statuscode=response.status_code
		self.assertEqual(statuscode,200)

	def test_calculate_content(self):
		tester = app.test_client(self)
		response = tester.get("/")
		self.assertEqual(response.content_type,"text/html; charset=utf-8")

	def test_index_content(self):
		tester = app.test_client(self)
		response = tester.get("/_calculate")
		self.assertEqual(response.content_type,"application/json")

if __name__ == "__main__":
	import xmlrunner
	runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    # unittest.main()


