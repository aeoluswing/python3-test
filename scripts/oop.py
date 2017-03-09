#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

class myselfclass(object):
    def __init__(self,x = 0.0,y = 0.0):
        self.__x = x
        self.__y = y

    def print_cls_name(self):
        print("__class__.__name__:",self.__class__.__name__)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y):
        self.__y = y

    @property
    def area(self):
        return self.__x * self.__y

    @property
    def circu(self):
        return 2 * (self.__x + self.__y)

if __name__ == '__main__':
    my_object = myselfclass(2,5)
    my_object.print_cls_name()
    print("x=",my_object.x)
    print("y=",my_object.y)
    print("area:",my_object.area)
    print("circu:",my_object.circu)
    print("==========================")
    my_object.x = 5
    my_object.y = 15
    print("x = ",my_object.x)
    print("y=",my_object.y)
    print("area:",my_object.area)
    print("circu:",my_object.circu)

