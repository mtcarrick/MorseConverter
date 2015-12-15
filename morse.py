#!/usr/bin/python3

import re

def convToMorse(str):

    morseDict = {'a':'.-', 'b':'-...', 'c':'-.-.',
                 'd':'-..', 'e':'.', 'f':'..-.',
                 'g':'--.', 'h':'....', 'i':'..',
                 'j':'.---', 'k':'-.-', 'l':'.-..',
                 'm':'--', 'n':'-.', 'o':'---',
                 'p':'.--.', 'q':'--.-', 'r':'.-.',
                 's':'...', 't':'-', 'u':'..-',
                 'v':'...-', 'w':'.--', 'x':'-..-',
                 'y':'-.--', 'z':'--..',

                 '1':'.----', '2':'..---', '3':'...--',
                 '4':'....-', '5':'.....', '6':'-....',
                 '7':'--...', '8':'---..', '9':'----.',
                 '0':'-----',

                 '.':'.-.-.-', ',':'--..--', '?':'..--..'}

    working = list(str)

    result = []

    for i in range(0,len(working)):
        result.append(morseDict[working[i].lower()]) # remember to convert to lower case
        
    return result    

def printMorse(list):

    str = ""
    for i in range(0,len(list)):
       str = str + list[i] + " "

    print(str)

if __name__ == '__main__':
    str = input('Enter your string: ')

    try:
        printMorse(convToMorse(str))
    except:
        print('Error! Can only take messages containing:\n\tLetters a-z\n\tDigits 1-9\n\tSpecial characters ? , .')
        input()
