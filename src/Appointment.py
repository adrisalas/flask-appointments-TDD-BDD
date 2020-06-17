#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__      = "Adrian Salas"

import src

class Appointment():
    def __init__(self,patient,workingTime):
        self.patient = patient
        self.workingTime = workingTime

    @property
    def patient(self): 
         return self._patient

    @patient.setter
    def patient(self,patient):
        if(type(patient) is not src.Patient.Patient):
            raise TypeError("patient must be a Patient")
        self._patient = patient

    @property
    def workingTime(self): 
         return self._workingTime

    @workingTime.setter
    def workingTime(self,workingTime):
        if(type(workingTime) is not src.WorkingTime.WorkingTime):
            raise TypeError("workingTime must be a WorkingTime")
        self._workingTime = workingTime

