import unittest

from app import app


class TestViews(unittest.TestCase):
    def test_home_page(self):
        with app.test_client() as client:
            res = client.get("/")

            self.assertEqual(res.status_code, 200, "should be 200 OK")
            self.assertIn(b"<h1>Welcome to the Friendster!</h1>", res.data)

    def test_about_page(self):
        with app.test_client() as client:
            res = client.get("/about")

            self.assertEqual(res.status_code, 200, "should be 200 OK")
            self.assertIn(b"<h1>About Friendster</h1>", res.data)

    def test_terms_page(self):
        with app.test_client() as client:
            res = client.get("/terms")

            self.assertEqual(res.status_code, 200, "should be 200 OK")
            self.assertIn(b"<h1>Terms and Conditions</h1>", res.data)
