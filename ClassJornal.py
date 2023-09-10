class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_evaluations(self, lecturer, course, grade: int):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
                and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and isinstance(self, Reviewer):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Новые классы
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)



sergey_brin = Student('Sergey', 'Brin', 'male')
sergey_brin.courses_in_progress += ['Python']

larry_page = Student('Larry', 'Page', 'male')
larry_page.courses_in_progress += ['C++']

steve_jobs = Lecturer('Steve', 'Jobs')
steve_jobs.courses_attached += ['Python']

bill_gates = Reviewer('Bill', 'Gates')
bill_gates.courses_attached += ['C++']

sergey_brin.lecturer_evaluations(steve_jobs, 'Python', 10)
sergey_brin.lecturer_evaluations(steve_jobs, 'Python', 10)
sergey_brin.lecturer_evaluations(steve_jobs, 'Python', 10)

bill_gates.rate_hw(larry_page, 'C++', 10)
bill_gates.rate_hw(larry_page, 'C++', 10)
bill_gates.rate_hw(larry_page, 'C++', 10)

print(steve_jobs.grades)
print(larry_page.grades)
