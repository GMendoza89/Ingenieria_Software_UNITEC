#!/usr/bin/python3
import menu
import alumno
run = True
runStudent = False
option = 0
dataBase = "/Users/gustavomendoza/Library/CloudStorage/OneDrive-LaureateMexico/Materias/05 - ICM002 - Ingenieria de software/Material/Programas/python/Sistema 02/database/students.txt"

while run:
    menu.consoleClear()
    option = menu.mainMenu()
    if option == 1:
        runStudent = True
        while runStudent:
            menu.consoleClear()
            studentOption = menu.studentMenu()
            if studentOption == 1:
                alumno.toRegisterStudent(dataBase)
            elif studentOption == 2:
                alumno.printStudentList(dataBase)
            elif studentOption == 3:
                alumno.unsubscribeStudent(dataBase)
            elif studentOption == 4:
                print("salir")
                runStudent = False
            else:
                menu.printError01()
    elif option == 2:
        print("En construcción")
    elif option == 3:
        print("En construcción")
    elif option == 4:
        print("En construcción")
    elif option == 5:
        menu.consoleClear()
        menu.goodBye()
        run = False
        
