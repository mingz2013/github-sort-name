# -*- coding:utf-8 -*-
"""
"""
__date__ = "15/07/2017"
__author__ = "zhaojm"

import requests

letters = [chr(i) for i in range(97, 123)]

numbers = range(10)


def check_name(name):
    # time.sleep(1)
    # print name
    url = "https://github.com/%s" % name
    response = requests.get(url)
    print response.status_code, url


def generate_len_names(length):
    if length == 0:
        pass
    elif length == 1:
        for l1 in letters:
            yield l1
    else:
        for l1 in letters:
            for l2 in generate_len_names(length - 1):
                yield l1 + l2


def generate_names(length):
    for l in range(length):
        for name in generate_len_names(l + 1):
            yield name


if __name__ == '__main__':
    for name in generate_names(2):
        check_name(name)
