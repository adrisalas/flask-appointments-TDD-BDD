#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__      = "Adrian Salas"

import datetime
import src

class WorkingTime():
    def __init__(self,hour,minute):
        self.timeDate = datetime.datetime(1970,1,1,hour=hour,minute=minute)
        self.appointment = None
    
    @property
    def timeDate(self): 
         return self._timeDate
         
    @timeDate.setter
    def timeDate(self,timeDate):
        if(type(timeDate) is not datetime.datetime):
            raise TypeError("timeDate must be a datetime.datetime")
        self._timeDate = timeDate

    @property
    def appointment(self): 
         return self._appointment

    @appointment.setter
    def appointment(self,appointment):
        if(type(appointment) is not src.Appointment.Appointment and appointment is not None):
            raise TypeError("appointment must be Appointment or None")
        self._appointment = appointment

    def __str__(self):
        return self.timeDate.strftime("%H:%M")

    