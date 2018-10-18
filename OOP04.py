#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : OOP04.py
# Author: roohom
# Date  : 2018/10/17 0017

# 构造函数


class Student(object):
    def __init__(self, first ="", last ="", id=0):
        self.firstnamestr = first
        self.lasnamestr = last
        self.idint = id


a = Student()
print(a.firstnamestr)
b = Student(first="HELLO", last="Python")
print(b.firstnamestr, b.lasnamestr)

print("=" * 30)
# 析构函数

class Car:
    def __init__(self, n):
        self.num = n
        print("编号为", self.num, "的对象born了！")
    def __del__(self):
        print("编号为", self.num, "的对象dead了！")

car1 = Car(1)
car2 = Car(2)
del car1
del car2


class InstCt(object):
    count = 0

    def __init__(self):
        InstCt.count += 1

    def __del__(self):
        InstCt.count -= 1

    def howMany(self):
        return InstCt.count
a = InstCt()
b = InstCt()
print(b.howMany())
print(a.howMany())
del b
print(a.howMany())
del a
print(InstCt.count)