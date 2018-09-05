# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 22:01:01 2018

@author: 2017VaioPro
"""

class Member:
    name = ''
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sayName(self):
        print(self.name)

taro = Member(age=1,name="taro")
taro.sayName()    