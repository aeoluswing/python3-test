#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class A():
    def __init__(self):
        print("class name: ",self.__class__.__name__)

class B(A):
    def __init__(self):
        return super(__class__,self).__init__()

class C(A):
    def __init__(self):
        print("class name: C")

class D(B,C):
    def __init__(self):
        return super(__class__,self).__init__()

if __name__=='__main__':
    objd = D()
    print(objd.__class__.__mro__)
    print("result:",issubclass(B,D))