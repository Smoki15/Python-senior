class Student:
    '''Constructor'''
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


    def print_info(self):
        print(f'I am {self.name}, I am {self.age} yers old, I from {self.country}')

first_student = Student('danil',12, 'Ukraine')
second_student = Student('Vasya',22, 'Poland')
third_student = Student('Petya',32, 'USA')
fourth_student= Student('Artur', 18, 'China')

first_student.print_info()
second_student.print_info()
third_student.print_info()
fourth_student.print_info()