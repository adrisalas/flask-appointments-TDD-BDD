import unittest

from app import app


class FlaskTest(unittest.TestCase):

    def test_hello(self):
        sut = app.test_client(self)
        response = sut.get('/hello', content_type='html/text')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_index(self):
        sut = app.test_client(self)
        response = sut.get('/', content_type='html/text')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'COVID-19',response.data)


if __name__ == '__main__':
    unittest.main()