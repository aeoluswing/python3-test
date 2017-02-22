#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys,unicodedata

def print_unicode_table(words):
    filename = "unicode-table.txt"
    fh = open(filename, "w", encoding="utf8")
    fh.write("decimal     hex  chr {0:^40}".format("name"))
    fh.write("-------    ----- --- {0:-<40}".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode)

    while code < end:
        c = chr(code)
        name = unicodedata.name(c,"*** unknown ***")
        result = True
        for word in words:
            if word not in name.lower():
                result = False
                break
        if result:
            #if use print,a unicodeTypeError will raise because of the auto transforation to system default encoding.insead,use write
            fh.write("{0:7} {0:5X} {0:^3c} {1}".format(code,name.title()))
        code += 1

if __name__ == '__main__':
    #print("locale.getdefaultlocale():",locale.getdefaultlocale())
    print("sys.getfilesystemencoding():",sys.getfilesystemencoding())
    print("stdout.encoding:",sys.stdout.encoding)
    print("stdin.encoding:",sys.stdin.encoding)
    print("sys.getdefaultencoding():",sys.getdefaultencoding())
    words = []
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h","--help"):
            print("usage:{0} [lower string array]".format(sys.argv[0]))
            words = None
        else:
            for word in sys.argv[1:]:
                words.append(word.lower())
    if words is not None:
        print_unicode_table(words)