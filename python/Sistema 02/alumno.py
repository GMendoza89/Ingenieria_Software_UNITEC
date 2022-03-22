import dictionary
import menu
STUDENTS = []

dt = dictionary.idiom_es
class studen():
    def __init__(self) -> None:
        self.lastname    = "Perez"
        self.name        = "Francisco"
        self.enrollment  = 0
        self.phoneNumber = "0000000000"
    def __init__(self,enrollment,lastname,name,phoneNumber) -> None:
        self.lastname    = lastname
        self.name        = name
        self.enrollment  = enrollment
        self.phoneNumber = phoneNumber

def upgradeSetudentDB(database):
    STUDENTS.clear()
    file = open(database,'r+')
    for line in file:
        studentAux = line.split()
        STUDENTS.append(studen(int(studentAux[0]),studentAux[1],studentAux[2],studentAux[3]))
    file.close()

def updateStudentDB(database):
    file = open(database,'w+')
    if file.closed:
        return False
    for student in STUDENTS:
        line = str(student.enrollment)+" "+student.lastname+" "+student.name+" "+student.phoneNumber+"\n"
        file.write(line)
    
    file.close()
    
    return True

def saveStudent(database,std):
    dbsize = len(STUDENTS)
    STUDENTS.append(std)
    update = updateStudentDB(database)
    if dbsize+1 != len(STUDENTS):
        return False
    elif not update:
        return False
    else:
        return True

def getEnrollmentNumber(database):
    upgradeSetudentDB(database)
    enrollmentNumber = len(STUDENTS)
    if enrollmentNumber == 0:
        enrollmentNumber = 1
    else:

        enrollmentNumber = STUDENTS[len(STUDENTS)-1].enrollment + 1
    return enrollmentNumber

def toRegisterStudent(database):
    menu.consoleClear()
    print(dt['toRegisterLastName'])
    lastn = input()
    print(dt['toRegisterName'])
    n = input()
    print(dt['toRegisterPhone'])
    phn = input()
    number = getEnrollmentNumber(database)
    newStudent = studen(number,lastn,n,phn)
    studentSaved =saveStudent(database,newStudent) 
    if studentSaved:
        menu.consoleClear()
        print(dt['succesfullRegister'],' ',newStudent.enrollment)
    else:
        menu.consoleClear()
        print(dt['failedRegister'])
    print(dt['textContinue'])
    input()

def unsubscribeStudent(database):
    menu.consoleClear()
    print(dt['searchEnrrollNumber'])
    number = int(input())
    upgradeSetudentDB(database)
    index = 0
    found = False
    studentAux = STUDENTS[0]
    for student in STUDENTS:
        index =+ 1
        if student.enrollment == number:
            found = True
            studentAux = student
            break
    if found:
        STUDENTS.remove(studentAux)
        updateStudentDB(database)
        print(dt['withdraw'])
        menu.inputContinue()
    else:
        print(dt['notFound'])
        menu.inputContinue()

def printStudentList(database):
    upgradeSetudentDB(database)
    menu.consoleClear()
    for student in STUDENTS:
        line = str(student.enrollment)+" "+student.lastname+" "+student.name+" "+student.phoneNumber+"\n"
        print(line)
    menu.inputContinue()

             


        
            
            














    