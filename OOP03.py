#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : OOP03.py
# Author: roohom
# Date  : 2018/10/17 0017

# 类的方法

class A(object):
    def foo(self,x):
        print("Executing foo{0}{1}".format(self, x))

    @classmethod  # 声明类方法
    def class_foo(cls, x):
        print("Executing class_foo{0}{1}".format(cls, x))

    @staticmethod  # 声明静态方法
    def static_foo(x):
        print("Executing static_foo{0}".format(x))


if __name__ == '__main__':
    a = A()
    a.foo(1)
    a.class_foo(1)
    A.class_foo(1)
    a.static_foo(1)
    A.static_foo(1)

print("=" * 30)


class Fruit:
    price = 0

    def __init__(self):

        self.__color = "red"
        self.__city = "Shanghai"

    def __outputColor(self):
        print(self.__color)

    def __outputCity(self):
        print(self.__city)

    def output(self):
        self.__outputColor()
        self.__outputCity()
    @staticmethod
    def getprice():
        return Fruit.price
    @staticmethod
    def setprice(p):
        Fruit.price = p


if __name__ == '__main__':
    apple = Fruit()
    apple.output()
    print(Fruit.getprice())
    Fruit.setprice(9)
    print(Fruit.getprice())
