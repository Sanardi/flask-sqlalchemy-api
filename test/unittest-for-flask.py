import unittest
import testAPI


class FlaskAPITests(unittest.TestCase):
    """Unit tests for Flask-tech-test that requires an internet connection"""
    

    def test_request1(self):
        data_expected = {'content': 'This is a post body',
 'id': 1,
 'regions': [{'code': 'AU', 'id': 1, 'name': 'Australia'},
  {'code': 'UK', 'id': 2, 'name': 'United Kingdom'}],
 'title': 'Post 1'}
        bla_get = TestAPI(url = "http://161.35.201.165:5555/articles/1")
        response = bla_get.test_get()
        self.assertEqual(response, data_expected)

    def test_request2(self):
        data_expected = '{"content":"Hello, this is a test","id":7,"regions":[],"title":"Sample Article"}\n'
        bla_get = TestAPI()
        response = bla_get.test_post()
        self.assertEqual(response, data_expected)



if __name__ == '__main__':
    unittest.main(buffer=True)
