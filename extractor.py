#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import Counter


def extractor():
    pass_list = open('pass_all.txt').read()
    unsorted_list = pass_list.split('\n')
    sorted_list = sorted(unsorted_list)
    pcount_dict = Counter(sorted_list)
    new_list = open('pass_all.txt', 'w')

    for pwd in pcount_dict:
        new_list.write(pwd[0] + ' ' + str(pwd[1]) + '\n')

    new_list.close()
    print('Done!')


def extract_from_list():
    pooltxt = open('list.txt').read()
	lines = pooltxt.split('\n')
	pool = map(lambda x: x.split(' '), lines)
    new_list = open('pass_all.txt', 'w')

    for cred in pool:
        new_list.write(cred[1] + '\n')

    new_list.close()

    pass_list = open('pass_all.txt').read()
    sorted_list = sorted(pass_list)
    count = Counter(sorted_list)
    new_list = open('pass_list.txt', 'w')
    prev = ""
    
    for pwd in sorted_list:
        if pwd == prev:
        	continue
        else:
        	new_list.write(pwd + ' ' + str(count[pwd]) + '\n')

    new_list.close()
    print('Done!')


# extractor()

extract_from_list()
