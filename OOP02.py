#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : OOP02.py
# Author: roohom
# Date  : 2018/10/17 0017

# 实例属性和类属性

class Product:
    price = 100

    def __init__(self,c):
        self.color = c


Product1 = Product("red")
Product2 = Product("Yellow")
print(Product1.color,Product2.color)
Product.price = 998
Product.name = "Gold"
Product1.color = "gold"
print(Product.name, Product1.price, Product1.color)
print(Product.name, Product2.price, Product2.color)

print("="*20)
# 私有在类外不能直接访问，Python提供了访问私有属性的方法，供于程序的测试和调试


class Food:
    def __init__(self):
        self.__color = "red"
        self.price = 2799


apple = Food()
apple.price = 9688
print(apple.price, apple._Food__color)          # 访问私有成员
apple._Food__color = "Blue"
print(apple.price, apple._Food__color)
print(apple._Food__color)
