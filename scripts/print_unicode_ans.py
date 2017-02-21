#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys,unicodedata

def print_unicode_table(words):
    print("decimal     hex  chr {0:^40}".format("name"))
    print("-------    ----- --- {0:-<40}".format(""))
    code = ord(" ")
    end = 127

    while code < end:
        c = chr(code)
        name = unicodedata.name(c,"*** unknown ***")
        result = True
        for word in words:
            if word not in name.lower():
                result = False
        if result:
            print("{0:7} {0:5X} {0:^3c} {1}".format(code,name.title()))
        code += 1

if __name__ == '__main__':
    words = []
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h","--help"):
            print("usage:{0} [lower string array]".format(sys.argv[0]))
            words = None
        else:
            for word in sys.argv[1:]:
                words.append(word)
    if words:
        print_unicode_table(words)