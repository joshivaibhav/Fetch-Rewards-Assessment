try:
    import unittest
    import json
    from api_server import app
except Exception as e:
    print("Some modules are missing {}". format(e))


class FlaskTestCase(unittest.TestCase):

    # Test /add_points route
    def test_add_points(self):
        tester = app.test_client(self)

        response = tester.post('http://127.0.0.1:5000/add_points',
        json = {"payer":"DANNON","points":"300","transaction_timestamp":"10/31 10AM"})
        self.assertEqual(response.status_code, 200)

        response = tester.post('http://127.0.0.1:5000/add_points',
        json={"payer": "UNILEVER", "points": "200", "transaction_timestamp": "10/31 11AM"})
        self.assertEqual(response.status_code, 200)

        response = tester.post('http://127.0.0.1:5000/add_points',
                               json={"payer": "DANNON", "points": "-200", "transaction_timestamp": "10/31 3PM"})
        self.assertEqual(response.status_code, 200)

        response = tester.post('http://127.0.0.1:5000/add_points',
                               json={"payer": "MILLER COORS", "points": "10000", "transaction_timestamp": "11/1 2PM"})
        self.assertEqual(response.status_code, 200)

        response = tester.post('http://127.0.0.1:5000/add_points',
                               json={"payer": "DANNON", "points": "1000", "transaction_timestamp": "11/2 2PM"})
        self.assertEqual(response.status_code, 200)

    # Test /deduct_points route
    def test_deduct_points(self):
        tester = app.test_client(self)
        response = tester.delete('http://127.0.0.1:5000/deduct_points', json={"points_to_deduct": "5000"})
        parsed_response = json.loads(response.data)
        print(parsed_response)
        self.assertEqual(response.status_code, 200)

    # Test /get_balance route
    def test_get_balance(self):
        tester = app.test_client(self)
        response = tester.get('http://127.0.0.1:5000/get_balance')
        parsed_response = json.loads(response.data)
        print(parsed_response)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()