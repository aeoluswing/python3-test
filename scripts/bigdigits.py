#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Digit print function for test

# define number array
Zero = [" 000 ",
        "0   0",
        "0   0",
        "0   0",
        "0   0",
        "0   0",
        " 000"]
One = [" 1 ",
       "11 ",
       " 1 ",
       " 1 ",
       " 1 ",
       " 1 ",
       "111"]
Two = [" 222 ",
       "2   2",
       "2  2 ",
       "  2  ",
       " 2   ",
       "2    ",
       "22222"]
Three = [" 333 ",
         "3   3",
         "   3 ",
         "  3  ",
         "   3 ",
         "3   3",
         " 333 "]
Four = ["    4 ",
        "   44 ",
        "  4 4 ",
        " 4  4 ",
        "444444",
        "    4 ",
        "    4 "]
Five = [" 5555 ",
        " 5    ",
        " 5    ",
        "  555 ",
        "     5",
        " 5   5",
        "  555 "]
Six = ["  666  ",
       " 6     ",
       " 6     ",
       " 6666  ",
       " 6   6 ",
       " 6   6 ",
       "  666  "]
Seven = ["7777777",
         "     7 ",
         "    7  ",
         "   7   ",
         "  7    ",
         " 7     ",
         "7      "]
Eight = ["  888  ",
         " 8   8 ",
         " 8   8 ",
         "  888  ",
         " 8   8 ",
         " 8   8 ",
         "  888  "]
Nine = ["  999  ",
        " 9   9 ",
        " 9   9 ",
        "  9999 ",
        "     9 ",
        "     9 ",
        "  999  "]

# define Dight array
Digits = [Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine]

# define print digits function
def printDigits():
    import sys
    try:
        digits = sys.argv[1]
        row = 0
        while row < 7:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                line += digit[row] + " "
                column += 1
            print(line)
            row += 1
    except IndexError:
        print("usage:bigdigit.py <number>")
    except ValueError as err:
        print(err)

if __name__ == '__main__':
    printDigits()
