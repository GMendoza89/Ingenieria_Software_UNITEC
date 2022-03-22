#!/usr/bin/python3
import menu
import ordenamiento

run = True

menu.languageOption(0)
while run:
    menu.consoleClear()
    opcion = menu.menu()
    if opcion == 1:
        menu.consoleClear()
        a,b,c = menu.optionOne()
        A,B,C = ordenamiento.sortOne(a,b,c)
        menu.consoleClear()
        menu.outputMessage(A,B,C)
        
    elif opcion == 2:
        menu.consoleClear()
        a,b,c = menu.optionTwo()
        A,B,C, = ordenamiento.sortTwo(a,b,c)
        menu.consoleClear()
        menu.outputMessage(A,B,C)
    elif opcion == 3:
        menu.consoleClear()
        menu.goodBye()
        menu.consoleClear()
        run = False
    else:
        menu.consoleClear()
        menu.printError01()

