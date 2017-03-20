#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decorator_1(func):
    print("decorator_1")
    print("decorator_1_plus")
    def wrapper(a,b):
        print("decorator_1_wrapper")
        func(a,b)
        print("wrapper_1")
    return wrapper

def decorator_2(func):
    print("decorator_2")
    print("decorator_2_plus")
    def wrapper(a,b):
        print("decorator_2_wrapper")
        func(a,b)
        print("wrapper_2")
    return wrapper

@decorator_1
@decorator_2
def addFunc(a,b):
    print("result is ",(a + b))

# deco_1(deco_2(addFunc))
addFunc(3,8)