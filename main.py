import QLSV.student as s

action = 0

while action >= 0:
    if action == 1:
        s.addStudent()
    elif action == 2:
        s.deleteStudent()
    elif action == 3:
        s.editStudent()
    elif action == 4:
        s.showStudent()
    elif action == 5:
        s.exitz()

    action = int(input('1. Add information student\n'
                   '2. Delete information student\n'
                   '3. Edit information student\n'
                   '4. Show information student\n'
                    '5. Exit!\n'
                    'Print your option: '))
    if action == 0:
        break