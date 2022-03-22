import os
import dictionary

dict = dictionary.idiom_es


def mainMenu():
    print(dict['mainPresentation'])
    print(dict['mainMenu'])
    opcion = input()
    opcion = int(opcion)
    return opcion
def studentMenu():
    print(dict['mainPresentation'])
    print(dict['studentMenu'])
    opcion = input()
    opcion = int(opcion)
    return opcion

def consoleClear():
    command = 'clear'
    if os.name in ('nt','dos'):
        command = 'cls'
    os.system(command)

def inputContinue():
    print(dict['textContinue'])
    input()

def printError01():
    consoleClear()
    print(dict['errorMesageOne'])
    inputContinue()

# def printError02():
#     consoleClear()
#     print(text['errorNumbers'])

def goodBye():
    print(dict['goodbyeMessage'])
    input()
