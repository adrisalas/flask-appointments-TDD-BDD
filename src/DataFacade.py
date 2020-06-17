#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__      = "Adrian Salas"

import src

allPatients = []
allDoctors = []

allDoctors.append(src.Doctor.Doctor("doctor@uma.es","1234","Paco","Durán Muñoz"))

allDoctors[0].workingDays.append(src.WorkingDay.WorkingDay(2020,6,1))
w0 = src.WorkingTime.WorkingTime(9,0)
allDoctors[0].workingDays[0].workingTimes.append(w0)
allDoctors[0].workingDays[0].workingTimes.append(src.WorkingTime.WorkingTime(9,30))
allDoctors[0].workingDays[0].workingTimes.append(src.WorkingTime.WorkingTime(10,0))
w1 = src.WorkingTime.WorkingTime(10,30)
allDoctors[0].workingDays[0].workingTimes.append(w1)
w2 = src.WorkingTime.WorkingTime(11,0)
allDoctors[0].workingDays[0].workingTimes.append(w2)

allDoctors[0].workingDays.append(src.WorkingDay.WorkingDay(2020,6,2))
allDoctors[0].workingDays[1].workingTimes.append(src.WorkingTime.WorkingTime(9,0))
w3 = src.WorkingTime.WorkingTime(9,30)
allDoctors[0].workingDays[1].workingTimes.append(w3)
allDoctors[0].workingDays[1].workingTimes.append(src.WorkingTime.WorkingTime(10,0))
w4 = src.WorkingTime.WorkingTime(10,30)
allDoctors[0].workingDays[1].workingTimes.append(w4)
allDoctors[0].workingDays[1].workingTimes.append(src.WorkingTime.WorkingTime(11,0))

allDoctors[0].workingDays.append(src.WorkingDay.WorkingDay(2020,6,3))
w5 = src.WorkingTime.WorkingTime(9,0)
allDoctors[0].workingDays[2].workingTimes.append(w5)
allDoctors[0].workingDays[2].workingTimes.append(src.WorkingTime.WorkingTime(9,30))
allDoctors[0].workingDays[2].workingTimes.append(src.WorkingTime.WorkingTime(10,0))
allDoctors[0].workingDays[2].workingTimes.append(src.WorkingTime.WorkingTime(10,30))
allDoctors[0].workingDays[2].workingTimes.append(src.WorkingTime.WorkingTime(11,0))

allDoctors[0].workingDays.append(src.WorkingDay.WorkingDay(2020,6,4))
allDoctors[0].workingDays[3].workingTimes.append(src.WorkingTime.WorkingTime(9,0))
allDoctors[0].workingDays[3].workingTimes.append(src.WorkingTime.WorkingTime(9,30))
allDoctors[0].workingDays[3].workingTimes.append(src.WorkingTime.WorkingTime(10,0))
allDoctors[0].workingDays[3].workingTimes.append(src.WorkingTime.WorkingTime(10,30))
allDoctors[0].workingDays[3].workingTimes.append(src.WorkingTime.WorkingTime(11,0))

allDoctors[0].workingDays.append(src.WorkingDay.WorkingDay(2020,6,5))
allDoctors[0].workingDays[4].workingTimes.append(src.WorkingTime.WorkingTime(9,0))
allDoctors[0].workingDays[4].workingTimes.append(src.WorkingTime.WorkingTime(9,30))
allDoctors[0].workingDays[4].workingTimes.append(src.WorkingTime.WorkingTime(10,0))
allDoctors[0].workingDays[4].workingTimes.append(src.WorkingTime.WorkingTime(10,30))
allDoctors[0].workingDays[4].workingTimes.append(src.WorkingTime.WorkingTime(11,0))

p0 = src.Patient.Patient("adri@uma.es","1234","Adri","Salas Troya",allDoctors[0])
p1 = src.Patient.Patient("jorge@uma.es","1234","Jorge","Salas Troya",allDoctors[0])
p2 = src.Patient.Patient("cristina@uma.es","1234","Cristina","Salas Troya",allDoctors[0])
p3 = src.Patient.Patient("alberto@uma.es","1234","Alberto","Salas Troya",allDoctors[0])
p4 = src.Patient.Patient("alicia@uma.es","1234","Alicia","Salas Troya",allDoctors[0])
p5 = src.Patient.Patient("victoria@uma.es","1234","Victoria","Salas Troya",allDoctors[0])
allPatients.append(p0)
allPatients.append(p1)
allPatients.append(p2)
allPatients.append(p3)
allPatients.append(p4)
allPatients.append(p5)

a1 = src.Appointment.Appointment(p1,w1)
p1.appointment_active = a1
w1.appointment = a1

a2 = src.Appointment.Appointment(p2,w2)
p2.appointment_active = a2
w2.appointment = a2

a3 = src.Appointment.Appointment(p3,w3)
p3.appointment_active = a3
w3.appointment = a3

a4 = src.Appointment.Appointment(p4,w4)
p4.appointment_active = a4
w4.appointment = a4

a5 = src.Appointment.Appointment(p5,w5)
p5.appointment_active = a5
w5.appointment = a5

def getAllPatients():
    return allPatients

def getAllDoctors():
    return allDoctors