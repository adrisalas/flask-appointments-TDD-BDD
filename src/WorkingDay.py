#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__      = "Adrian Salas"

import datetime

class WorkingDay():
    weekdays_esp = {
        0: "Domingo",
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sabado"
    }

    def __init__(self,year,month,day):
        self.dayDate = datetime.datetime(year,month,day)
        self.workingTimes = []

    @property
    def dayDate(self): 
         return self._dayDate
         
    @dayDate.setter
    def dayDate(self,dayDate):
        if(type(dayDate) is not datetime.datetime):
            raise TypeError("dayDate must be a datetime.datetime")
        self._dayDate = dayDate

    def __str__(self):
        weekday_en = int(self.dayDate.strftime("%w"))
        return "Día " + self.dayDate.strftime("%d/%m/%Y, " + WorkingDay.weekdays_esp[weekday_en])

    