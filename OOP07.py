#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : OOP07.py
# Author: roohom
# Date  : 2018/10/19 0019

# 使用特性进行属性存取控制
import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):                         # 圆的边到原点的距离
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi*(self.radius**2)


if __name__ == '__main__':
    circle = Circle(5, 6, 8)
    print(circle.radius)
    print(circle.distance_from_origin())
    print(circle.edge_distance_from_origin())

