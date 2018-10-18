#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : OOP05.py
# Author: roohom
# Date  : 2018/10/18 0018

#                                          继承                                            #


class Super:
    def method(self):
        print("In Super.method")


class Sub(Super):
    def method(self):
        print("Starting Sub.method")
        Super.method(self)
        print("Ending Sub.method")


s = Super()
s.method()
x = Sub()
x.method()

print("=" * 30)


# 类接口技术
'''
Super:       定义一个method函数以及在子类中期待一个动作的delegate
Inheritor：  没有提供任何新的变量名，因此会获得Super中定义的一切内容
Replacer ：  用自己的method覆盖Super的method
Extender ：  覆盖并回调默认method，从而定制Super的method
Provider ：  实现Super的delegate方法预期的action方法
'''
class Super:
    def method(self):
        print("In Super.method")

    def delegate(self):
        self.action()


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print("In Replacer.method")


class Extender(Super):
    def method(self):
        print("Starting Extender.method")
        Super.method(self)
        print("Ending Extender.method")


class Provider(Super):
    def action(self):
        print("In Provider.action")


if __name__ == '__main__':
    for i in (Inheritor, Replacer, Extender):
        print("\n" + i.__name__ + "......")
        i().method()
        print("\nProvider...")
        l = Provider()
        l.delegate()
        print("---------------")
