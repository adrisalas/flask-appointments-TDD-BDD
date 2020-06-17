import unittest
from .context import src
from src.Patient import Patient
from src.Appointment import Appointment
from src.Doctor import Doctor
from src.WorkingDay import WorkingDay
from src.WorkingTime import WorkingTime

class AppointmentTest(unittest.TestCase):
    def setUp(self):
        self.d1 = Doctor("uma","1234","Paco","Durán")
        self.p1 = Patient("email","1234","Adri","Salas",self.d1)
        self.d1.workingDays.append(WorkingDay(2020,6,1))
        self.wt1 = WorkingTime(9,0)
        self.d1.workingDays[0].workingTimes.append(self.wt1)

    def test_patient_init_Error(self):
        with self.assertRaises(TypeError):
            Appointment(None,None)

    def test_patient_getter(self):
        a = Appointment(self.p1, self.wt1)
        self.assertEqual(self.p1, a.patient)
    
    def test_patient_setter(self):
        p2 = Patient("email2","1234","Adri2","Salas",self.d1)
        a = Appointment(self.p1,self.wt1)
        a.patient = p2
        self.assertEqual(p2, a.patient)
    
    def test_patient_setter_Error(self):
        a = Appointment(self.p1,self.wt1)
        with self.assertRaises(TypeError):
            a.patient = "hello"

if __name__ == '__main__':
    unittest.main()