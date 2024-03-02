import unittest
import requests

class TestPrimeFunction(unittest.TestCase):
    
    def test_true_when_x_is_17(self):
        response = requests.get("http://localhost:5000/is_prime/17")
        result = response.json()

        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.headers['content-type'], 'application/json')
        self.assertTrue(result)

    def test_false_when_x_is_36(self):
        response = requests.get("http://localhost:5000/is_prime/36")
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertFalse(result)

    def test_true_when_x_is_13219 (self):
        response = requests.get("http://localhost:5000/is_prime/13219")
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()