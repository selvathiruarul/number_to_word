#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:31:10 2016

@author: selva
"""
WORDS = {'-': 'negative', 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
         8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
         14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 1000000: 'million'}


def convert(no, word=''):
    """
    Method to convert number to word
    :param no: 
    :param word: 
    :return: 
    """
    if no != 0:
        if no in WORDS:
            word += " " + WORDS[no]
        elif 20 < no < 100:
            if word != '':
                word += " " + WORDS[(no / 10) * 10]
            else:
                word = WORDS[(no / 10) * 10]
            word = convert(no % 10, word)
        elif 100 < no < 1000:
            if word != '':
                word += " " + WORDS[(no / 100)] + " " + WORDS[100]
            else:
                word = WORDS[(no / 100)] + " " + WORDS[100]
            word = convert(no % 100, word)
        elif 1000 < no < 1000000:
            if word != '':
                word += " " + convert(no / 1000) + " " + WORDS[1000]
            else:
                word = convert(no / 1000) + " " + WORDS[1000]
            word = convert(no % 1000, word)
        elif 1000000 < no < 1000000000:
            if word != '':
                word += " " + convert(no / 1000000) + " " + WORDS[1000000]
            else:
                word = convert(no / 1000000) + " " + WORDS[1000000]
            word = convert(no % 1000000, word)

    return word


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    if number < 0:
        english_words = convert(-number, WORDS['-'])
    elif number > 0:
        english_words = convert(number)
    else:
        english_words = WORDS[number]
    print(english_words)
