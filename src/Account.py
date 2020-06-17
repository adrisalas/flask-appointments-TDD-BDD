#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__      = "Adrian Salas"

class Account:
    def __init__(self,email,password):
        self.email = email
        self.password = password
    
    @property
    def email(self): 
         return self._email

    @email.setter
    def email(self,email):
        if(type(email) is not str):
            raise TypeError("Email must be a str")
        self._email = email

    @property
    def password(self): 
         return self._password

    @password.setter
    def password(self,password):
        if(type(password) is not str):
            raise TypeError("Password must be a str")
        self._password = password