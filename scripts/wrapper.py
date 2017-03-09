#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def deco_1(func):
    print("deco_1")
    print("deco_1_plus")
    def wrapper(a,b):
        print("deco_1_wrapper")
        func(a,b)
        print("wrapper_1")
    return wrapper

def deco_2(func):
    print("deco_2")
    print("deco_2_plus")
    def wrapper(a,b):
        print("deco_2_wrapper")
        func(a,b)
        print("wrapper_2")
    return wrapper

@deco_1
@deco_2
def addFunc(a,b):
    print("result is ",(a + b))

# deco_1(deco_2(addFunc))
addFunc(3,8)