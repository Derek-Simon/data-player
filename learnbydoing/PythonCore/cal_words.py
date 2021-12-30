#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Created by Derek on 2021/10/26
"""
-------------------------------------------------
File Name :  main
Description : words counts using python std library
Author : derek
Email : derek_simon@outlook.com
-------------------------------------------------
Change Activity:
    2021/10/26: create
-------------------------------------------------
"""


def words_count(words_str):
    '''
    a simple case for words counting
    :param words_str: a given sentence to be counted by words
    :return: a dict words with key is words and value is frequency
    '''
    words_dict = {}
    if words_str:
        # flow: lowercase, split, strip '.' & ',', add to dict
        words_list = words_str.lower().split()
        for word in words_list:
            clean_word = word
            if '.' in word:
                # replace it without '.' in place
                clean_word = word.split('.')[0]
            if ',' in word:
                # replace it without ',' in place
                clean_word = word.split(',')[0]
            words_dict[clean_word] = words_dict[clean_word] + 1 if word in words_dict.keys() else 1
        pass

    return words_dict


if __name__ == '__main__':
    new_sentence = "I do coding very often. I'm interested in coding to cope with finance or trading problem."
    output = words_count(new_sentence)
    print(output)
