import QLSV.data as d

def addStudent():
    print("Create new student")

    infor = {
        'id': '',
        'name': '',
        'age': ''
    }

    id = input('Enter IDs student: ')

    while True:
        student = findStudent(id)
        if student != False:
            id = input('The ID exists. Please re-enter id: ')
        else:
            break
    infor['id'] = id

    infor['name'] = input('Enter names student: ')
    infor['age'] = input('Enter ages student: ')

    # Save information's student
    d.listStudents.append(infor)

def findStudent(id):
    for i in range(0, len(d.listStudents)):
        if d.listStudents[i]['id']==id:
            return [i, d.listStudents[i]]
    return False

def deleteStudent():
    print('Delete informations students')

    id = input('Enter IDs student to delete: ')

    student = findStudent(id)

    if student != False:
        d.listStudents.remove(student[1])
        print('Deleted!')
    else:
        print('Cant find information student!')

def showStudent():
    print('Show the informations student')

    for i in range(0, len(d.listStudents)):
        print('|', d.listStudents[i]['id'], '|', d.listStudents[i]['name'], '|', d.listStudents[i]['age'], '|')

def editStudent():
    print('Update informations student')
    id = input('Enter IDs student: ')
    student = findStudent(id)

    if student == False:
        print('Cant find informations student!')
    else:
        option = int(input('Edition information student\n 1. Name...\n 2. Age...\n '
                       'Enter your option: '))
        if option == 1:
            name = input('Enter name: ')
            student[1]['name'] = name
            d.listStudents[student[0]] = student[1]
        elif option == 2:
            age = input('Enter age: ')
            student[1]['age'] = age
            d.listStudents[student[0]] = student[1]

def exitz():
    exit()
