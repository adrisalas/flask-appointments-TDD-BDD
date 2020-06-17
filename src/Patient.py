#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__      = "Adrian Salas"

import src

class Patient(src.Account.Account):
    def __init__(self,email,password,name,surname,doctor):
        super().__init__(email,password)
        self.name = name
        self.surname = surname
        self.doctor = doctor
        self.appointments_inactive = []
        self.appointment_active = None

    @property
    def name(self): 
         return self._name

    @name.setter
    def name(self,name):
        if(type(name) is not str):
            raise TypeError("Name must be a str")
        self._name = name
    
    @property
    def surname(self): 
         return self._surname

    @surname.setter
    def surname(self,surname):
        if(type(surname) is not str):
            raise TypeError("Surname must be a str")
        self._surname = surname

    @property
    def doctor(self): 
         return self._doctor

    @doctor.setter
    def doctor(self,doctor):
        if(type(doctor) is not src.Doctor.Doctor):
            raise TypeError("doctor must be a Doctor")
        self._doctor = doctor

    @property
    def appointment_active(self): 
         return self._appointment_active

    @appointment_active.setter
    def appointment_active(self,appointment_active):
        if(type(appointment_active) is not src.Appointment.Appointment and appointment_active is not None):
            raise TypeError("appointment_active must be Appointment or None")
        self._appointment_active = appointment_active

    def __str__(self):
        return self.surname + ", " + self.name