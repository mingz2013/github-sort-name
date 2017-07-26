# -*- coding:utf-8 -*-
"""
"""
__date__ = "15/07/2017"
__author__ = "zhaojm"

import codecs

import requests

import time

import datetime

import functools


letters = [chr(i) for i in range(97, 123)]

numbers = range(10)

letters += numbers


def check_name(name):
    url = "https://github.com/%s" % name
    try:
        response = requests.get(url)
        return response.status_code, url
    except Exception, e:
        return e.message, url


def generate_len_names(length):
    if length == 0:
        pass
    elif length == 1:
        for l1 in letters:
            yield l1
    else:
        for l1 in letters:
            for l2 in generate_len_names(length - 1):
                yield "%s%s" % (l1, l2)


def generate_names(length):
    for l in range(length):
        for name in generate_len_names(l + 1):
            yield name


test_len = 3


def print_name(f, name):
    # print >> f, check_name(name)
    # print >>f, name
    # print name
    pass


def main_loop(func):
    for name in generate_names(test_len):
         # yield func(name)
         func(name)


def main():
    with codecs.open('result.log', mode='w', encoding='utf8') as f:
        func = functools.partial(print_name, f)
        loop = main_loop(func)
        if loop:
            for _ in main_loop(func):
                pass


if __name__ == '__main__':
    begin = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    delta = end - begin
    print begin.strftime('%Y-%m-%d %H:%M:%S.%f')
    print end.strftime('%Y-%m-%d %H:%M:%S.%f')
    print delta.total_seconds()

