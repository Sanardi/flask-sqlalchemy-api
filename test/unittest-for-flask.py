import unittest
import testAPI


class FlaskAPITests(unittest.TestCase):
    """Unit tests for Flask-tech-test that requires an internet connection"""
    

    def test_request1(self):
        data_expected = 200
        test1 = testAPI.TestAPI()
        response = test1.test_get()
        self.assertEqual(response, data_expected)

    def test_request2(self):
        data_expected = 200
        test2 = testAPI.TestAPI()
        response = test2.test_post()
        self.assertEqual(response, data_expected)



if __name__ == '__main__':
    unittest.main(buffer=True)
