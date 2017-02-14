#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input_array(msg):
    array = []
    while True:
        try:
            number = input(msg)
            if not number:
                break
            digit = int(number)
            array.append(digit)
        except ValueError:
            print("usage:input must be number")
    print("numbers:",array)
    return array

def sort_array(array):
    try:
        for i in range(len(array)-1):
            for n in range(i+1,len(array)):
                if array[i] > array[n]:
                    middle = array[i]
                    array[i] = array[n]
                    array[n] = middle
    except IndexError as err:
        print(err)
    return array

def get_result(array):
    sorted_array = sort_array(array)
    count = sum = mean = middle = 0
    lowest = highest = 0
    try:
        count = len(sorted_array)
        for i in range(count):
            sum += sorted_array[i]
        lowest = sorted_array[0]
        highest = sorted_array[-1]
        mean = sum/count
        if count%2:
            middle = sorted_array[count//2]
        else:
            middle = (sorted_array[count//2 - 1] + sorted_array[count//2])/2
        print("count = " + str(count) + " sum = " + str(sum) + " lowest = " + str(lowest) + " highest = " + str(highest) + " mean = " + str(mean) + " middle = " + str(middle))
    except IndexError as err:
        print(err)

if __name__ == '__main__':
    array = get_input_array("enter a number or Enter to finish:")
    get_result(array)