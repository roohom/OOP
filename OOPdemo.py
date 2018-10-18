#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : OOPdemo.py
# Author: roohom
# Date  : 2018/10/17 0017


class Firstclass:
    def setdata(self,value):
        self.data=value
    def display(self):
        print(self.data)


x = Firstclass()
y = Firstclass()

x.setdata("red")
y.setdata(23)
x.display()
y.display()

x.data="new"
x.display()
