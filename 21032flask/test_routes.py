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

if __name__ == "__main__":
	unittest.main()


