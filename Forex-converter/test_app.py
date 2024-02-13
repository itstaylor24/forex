from app import app
from unittest import TestCase

class ConversionTestCase(TestCase):
    def test_form_show(self):
        """tests to see if form is displayed correctly"""
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Currency Conversion Form</h1>', html)

    def test_form_from(self):
        """tests if conversion is accurately carried out if all form data is entered correctly"""
        with app.test_client() as client:
            res = client.post('/convert', data ={'from': 'USD', 'to': 'USD', 'amount': 1}, follow_redirects = True)
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn("<p>1.0 USD to USD is 1 USD</p>", html)

    def test_redirect(self):
        """tests if redirected back to / if missing info in input"""
        with app.test_client() as client:
            res = client.post('/convert', data ={'from': '', 'to': 'USD', 'amount': 1}, follow_redirects = True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 302)
            self.assertIn("<p>must input data in all spaces</p>", html)

    def test_redirect2(self):
        """tests to see if redirected back to / if invalid currency code entered """
        with app.test_client() as client:
            res = client.post('/convert', data ={'from': 'USD', 'to': 'rr', 'amount': 1}, follow_redirects = True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 302) 
            self.assertIn("<p>'to' currency not in database</p>", html)


    def test_redirect3(self):
        """tests if redirected back to / if improper numerical amount is entered"""
        with app.test_client() as client:
            res = client.post('/convert', data ={'from': 'USD', 'to': 'GBP', 'amount': 'xxx'}, follow_redirects = True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 302)  
            self.assertIn("<p>amount input is either empty or not a proper numerical amount</p>", html)
             
