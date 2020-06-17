#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__      = "Adrian Salas"

import src

class Doctor(src.Account.Account):
    def __init__(self,email,password,name,surname):
        super().__init__(email,password)
        self.name = name
        self.surname = surname
        self.workingDays = []

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

    def __str__(self):
        return "Dr. " + self.surname + ", " + self.name