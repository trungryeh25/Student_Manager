class Student:
    def addStudent(self):
        print("Create new student")

        infor = {
            'id': '',
            'name': '',
            'age': ''
        }

        id = input('Enter IDs student: ')

        while True:
            student = self.findStudent(id)
            if student != False:
                id = input('The ID exists. Please re-enter id: ')
            else:
                break
        infor['id'] = id

        infor['name'] = input('Enter names student: ')
        infor['age'] = input('Enter ages student: ')

        # Save information's student
        self.listStudents.append(infor)

    def findStudent(self, id):
        for i in range(0, len(self.listStudents)):
            if self.listStudents[i]['id'] == id:
                return [i, self.listStudents[i]]
        return False

    def deleteStudent(self):
        print('Delete informations students')

        id = input('Enter IDs student to delete: ')

        student = self.findStudent(id)

        if student != False:
            self.listStudents.remove(student[1])
            print('Deleted!')
        else:
            print('Cant find information student!')

    def showStudent(self):
        print('Show the informations student')

        for i in range(0, len(self.listStudents)):
            print('|', self.listStudents[i]['id'], '|', self.listStudents[i]['name'], '|', self.listStudents[i]['age'], '|')

    def editStudent(self):
        print('Update informations student')
        id = input('Enter IDs student: ')
        student = self.findStudent(id)

        if student == False:
            print('Cant find informations student!')
        else:
            option = int(input('Edition information student\n 1. Name...\n 2. Age...\n '
                               'Enter your option: '))
            if option == 1:
                name = input('Enter name: ')
                student[1]['name'] = name
                self.listStudents[student[0]] = student[1]
            elif option == 2:
                age = input('Enter age: ')
                student[1]['age'] = age
                self.listStudents[student[0]] = student[1]

    def exitz(self):
        exit()