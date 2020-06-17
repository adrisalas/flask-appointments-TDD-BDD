import unittest
from .context import src
from src.Account import Account

class AccountTest(unittest.TestCase):
    def test_init_variables(self):
        email = "adri@sample.com"
        password = "1234"
        acc = Account(email,password)

        self.assertEqual(email, acc.email)
        self.assertEqual(password, acc.password)

    def test_init_emailIsNone(self):
        email = None
        password = "1234"
        with self.assertRaises(TypeError):
            Account(email,password)
    
    def test_init_passwordIsNotString(self):
        email = "adri@sample.com"
        password = 1234
        with self.assertRaises(TypeError):
            Account(email,password)

    def test_init_passwordIsNone(self):
        email = "adri@sample.com"
        password = None
        with self.assertRaises(TypeError):
            Account(email,password)
    
    def test_init_emailIsNotString(self):
        email = 1234
        password = "1234"
        with self.assertRaises(TypeError):
            Account(email,password)

if __name__ == '__main__':
    unittest.main()