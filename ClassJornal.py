def mean(self):
    if len(self.grades.values()) == 0:
        return 0
    sum_all_grade = 0
    len_all_grade = 0
    for val in self.grades.values():
        sum_all_grade += sum(val)
        len_all_grade += len(val)
    return sum_all_grade / len_all_grade


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}' \
               f'\nСредняя оценка за домашнее задание: {mean(self):.1f}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение возможно лишь с лекторами')
        if mean(self) < mean(other):
            print('Студенты лузеры!')
            return mean(self)
        else:
            print('Студенты рулят!')
            return mean(self)

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение возможно лишь с лекторами')
        if mean(self) > mean(other):
            print('Студенты рулят!')
            return mean(self)
        else:
            print('Студенты лузеры!')
            return mean(self)

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение возможно лишь с лекторами')
        if mean(self) <= mean(other):
            print('Студенты лузеры!')
            return mean(self)
        else:
            print('Студенты рулят!')
            return mean(self)

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение возможно лишь с лекторами')
        if mean(self) >= mean(other):
            print('Студенты рулят!')
            return mean(self)
        else:
            print('Студенты лузеры!')
            return mean(self)

    def lecturer_evaluations(self, lecturer, course, grade: int):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
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

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение возможно лишь со студентами')
        if mean(self) < mean(other):
            print('Лекторы лузеры!')
            return mean(self)
        else:
            print('Лекторы рулят!')
            return mean(self)

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение возможно лишь со студентами')
        if mean(self) > mean(other):
            print('Лекторы рулят!')
            return mean(self)
        else:
            print('Лекторы лузеры!')
            return mean(self)

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Сравнение возможно лишь со студентами')
        if mean(self) <= mean(other):
            print('Лекторы лузеры!')
            return mean(self)
        else:
            print('Лекторы рулят!')
            return mean(self)

    def __ge__(self, other):
        if not isinstance(other, Student):
            print('Сравнение возможно лишь со студентами')
        if mean(self) >= mean(other):
            print('Лекторы рулят!')
            return mean(self)
        else:
            print('Лекторы лузеры!')
            return mean(self)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {mean(self):.1f}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


sergey_brin = Student('Sergey', 'Brin', 'male')
sergey_brin.courses_in_progress += ['Python']
sergey_brin.finished_courses += ["Golang"]

larry_page = Student('Larry', 'Page', 'male')
larry_page.courses_in_progress += ['C++']
larry_page.finished_courses += ["Golang"]

steve_jobs = Lecturer('Steve', 'Jobs')
steve_jobs.courses_attached += ['Python']
steve_jobs.courses_attached += ['Swift']

bill_gates = Reviewer('Bill', 'Gates')
bill_gates.courses_attached += ['C++']

sergey_brin.lecturer_evaluations(steve_jobs, 'Python', 5)
sergey_brin.lecturer_evaluations(steve_jobs, 'Python', 10)
sergey_brin.lecturer_evaluations(steve_jobs, 'Python', 10)

sergey_brin.lecturer_evaluations(steve_jobs, 'Swift', 10)
sergey_brin.lecturer_evaluations(steve_jobs, 'Swift', 10)

bill_gates.rate_hw(larry_page, 'C++', 10)
bill_gates.rate_hw(larry_page, 'C++', 10)
bill_gates.rate_hw(larry_page, 'C++', 10)

print(steve_jobs.grades)
print(larry_page.grades)
print()
print(bill_gates)
print()
print(steve_jobs)
print()
print(larry_page)
print()
print(sergey_brin)
print()
print(larry_page >= steve_jobs)
print()
print(steve_jobs <= larry_page)
