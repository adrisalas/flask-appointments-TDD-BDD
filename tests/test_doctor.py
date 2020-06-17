import unittest
from .context import src
from src.Doctor import Doctor

class DoctorTest(unittest.TestCase):

    def test_init(self):
        d1 = Doctor("uma","1234","Paco","Durán")
        d1.email

if __name__ == '__main__':
    unittest.main()