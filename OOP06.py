#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : OOP06.py
# Author: roohom
# Date  : 2018/10/18 0018


# 子类与父类之间的关系

class Person(object):
    sex = "male"
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print("__init__(self) of Person")

    def Hello(self, friend):
        print("Hello,", friend)


class Student(Person):
    def __init__(self, num):
        self.number = num

    def fun(self):
        print(self.sex, self.name, self.number, self.age)


class Worker(Person):
    def __init__(self, company, age, name):
        self.company = company
        super(Worker, self).__init__(age, name)

    def fun(self):
        print(self.sex, self.name, self.company, self.age)

student1 = Student("20181018")
student1.name = "roohom"
student1.age = 21

student1.fun()
student1.Hello("Python")
worker = Worker("Xiaomi", 21, "LittleBAI")
worker.sex = "Female"
worker.fun()
worker.Hello("LittleRED")
