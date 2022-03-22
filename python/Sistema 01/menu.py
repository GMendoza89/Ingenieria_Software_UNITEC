import os
import textStrings

text = textStrings.text_en

def languageOption(idiom):
    if idiom == 0:
        text = textStrings.text_es
    elif idiom == 1:
        text =textStrings.text_en
    else: 
        text = textStrings.text_es

def menu():
    print(text['mainMenu'])
    print(text['mainOption'])
    opcion = input()
    opcion = int(opcion)
    return opcion

def consoleClear():
    command = 'clear'
    if os.name in ('nt','dos'):
        command = 'cls'
    os.system(command)

def inputContinue():
    print(text['textContinue'])
    input()

def printError01():
    consoleClear()
    print(text['errorOption'])
    inputContinue()

def printError02():
    consoleClear()
    print(text['errorNumbers'])

def differentABInput():
    banderaSalida = True
    a,b = 0,0
    while banderaSalida:
        print(text['inputA'])
        a = int(input())
        print(text['inputB'])
        b = int(input())
        if a == b:
            printError02()
        else:
            banderaSalida = False
    return a,b

def differentCInput(a,b):
    banderaSalida = True
    c = 0
    while banderaSalida:
        print(text['inputC'])
        c = int(input())
        if c == a or c == b:
            printError02()
        else:
            banderaSalida = False
    return c

def optionOne():
    a,b = differentABInput()
    c = differentCInput(a,b)
    return (a,b,c)

def optionTwo():
    print(text['inputA'])
    a = int(input())
    print(text['inputB'])
    b = int(input())
    print(text['inputC'])
    c = int(input())
    return (a,b,c)

def outputMessage(a,b,c):
    print(text['sortOutput'],a,", ",b,", ",c,", ")
    print(text['textContinue'])
    input()

def goodBye():
    print(text['goodbyeMessage'])
    input()
