import unittest
from .context import src
from src.WorkingDay import WorkingDay

class WorkingDayTest(unittest.TestCase):

    def test_str_wholeWeek(self):
        wd = WorkingDay(2020,5,24)
        self.assertEqual("Día 24/05/2020, Domingo",wd.__str__())
        wd = WorkingDay(2020,5,25)
        self.assertEqual("Día 25/05/2020, Lunes",wd.__str__())
        wd = WorkingDay(2020,5,26)
        self.assertEqual("Día 26/05/2020, Martes",wd.__str__())
        wd = WorkingDay(2020,5,27)
        self.assertEqual("Día 27/05/2020, Miércoles",wd.__str__())
        wd = WorkingDay(2020,5,28)
        self.assertEqual("Día 28/05/2020, Jueves",wd.__str__())
        wd = WorkingDay(2020,5,29)
        self.assertEqual("Día 29/05/2020, Viernes",wd.__str__())
        wd = WorkingDay(2020,5,30)
        self.assertEqual("Día 30/05/2020, Sabado",wd.__str__())

    def test_init_Error_Month13(self):
        with self.assertRaises(ValueError):
            WorkingDay(2020,13,24)

    def test_init_Error_Month0(self):
        with self.assertRaises(ValueError):
            WorkingDay(2020,0,24)

    def test_init_Day29February2020(self):
        WorkingDay(2020,2,29)

    def test_error_Day29February2019(self):
        with self.assertRaises(ValueError):
            WorkingDay(2019,2,29)

if __name__ == '__main__':
    unittest.main()