#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

article = ["the","a"]
topic = ["cat","dog","man","woman"]
verb = ["sang","ran","jumped"]
adv = ["loudly","quietly","well","badly"]

statement_structure1 = [article,topic,verb,adv]
statement_structure2 = [article,topic,verb]
statement_structure = [statement_structure1,statement_structure2]

def get_statement_structure(array):
    index = 0
    try:
        index = random.randint(0,1)
    except IndexError as err:
        print(err)
    return array[index]

def get_statement(array):
    result = ''
    try:
        for i in range(len(array)):
            result += (random.choice(array[i]) + ' ')
    except IndexError as err:
        print(err)
    return result

def print_statement(array):
    try:
        for i in range(len(array)):
            print(array[i])
    except IndexError as err:
        print(err)

if __name__ == '__main__':
    number = input("input the time of the circulation:")
    digit = 0
    try:
        if not number:
            for i in range(5):
                structure = get_statement_structure(statement_structure)
                print(get_statement(structure))
        else:
            digit = int(number)
            for i in range(digit):
                structure = get_statement_structure(statement_structure)
                if i == (digit - 1):
                    print(get_statement(structure))
    except IndexError as err:
        print(err)

