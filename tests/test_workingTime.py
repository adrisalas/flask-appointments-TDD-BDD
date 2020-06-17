import unittest
from .context import src
from src.WorkingTime import WorkingTime

class WorkingTimeTest(unittest.TestCase):

    def test_str(self):
        wt = WorkingTime(20,20)
        self.assertEqual("20:20",wt.__str__())
        wt = WorkingTime(8,30)
        self.assertEqual("08:30",wt.__str__())
        wt = WorkingTime(9,59)
        self.assertEqual("09:59",wt.__str__())

    def test_init_Error_time2400(self):
        with self.assertRaises(ValueError):
            WorkingTime(24,00)

    def test_init_time0000(self):
        WorkingTime(00,00)

    def test_init_Error_time0060(self):
        with self.assertRaises(ValueError):
            WorkingTime(00,60)

if __name__ == '__main__':
    unittest.main()