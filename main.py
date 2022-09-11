class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


#оценка лекторам
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

#средняя оценка студента за ДЗ
    def average_grade(self):
        sum_gr = 0
        for self.grade in self.grades:
            sum_gr += sum(self.grade) / len(self.grade)
        return round(sum_gr / len(self.grades), 1)



#магический метод str студент
    def __str__(self):
        return (f'Имя: {self.name} \n Фамилия: {self.surname} \nСредняя оценка за домашние задания:{self.average_grade}'
                f'\nКурсы в процессе изучения:{self.courses_in_progress} \nЗавершенные курсы:{self.finished_courses}')

# сравнение средней оценки между студентами
    def __lt__(self, Student):
        return self.average_grade < Student.average_grade

    def __gt__(self, Student):
        return self.average_grade > Student.average_grade

    def __eq__(self, Student):
        return self.average_grade == Student.average_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

#средняя оценка лектора за ДЗ
    def average_grade(self):
        sum_gr = 0
        for self.grade in self.grades:
            sum_gr += sum(self.grade) / len(self.grade)
        return round(sum_gr / len(self.grades), 1)

#магический метод str лектор
    def __str__(self):
        return (f'Имя: {self.name} \n Фамилия: {self.surname} \nСредняя оценка за лекции:{self.average_grade}')


class Reviewer(Mentor):
# оценка студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        # магический метод str лектор
    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}')

student_1 = Student('Ivan', 'Ivanov', 'm')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Sidor', 'Sidorov', 'm')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer('Petr', 'Petrov')
reviewer_1.courses_attached += ['Python', 'Git']

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python', 'Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Git', 7)

reviewer_1.rate_hw(student_2, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Git', 6)
reviewer_1.rate_hw(student_2, 'Git', 8)

student_1.rate_lec(lecturer_1 , 'Python', 10)
student_1.rate_lec(lecturer_1 , 'Python', 9)
student_1.rate_lec(lecturer_1 , 'Python', 9)

student_2.rate_lec(lecturer_1 , 'Python', 10)
student_2.rate_lec(lecturer_1 , 'Python', 10)
student_2.rate_lec(lecturer_1 , 'Python', 7)

student_1.rate_lec(lecturer_1 , 'Git', 7)
student_1.rate_lec(lecturer_1 , 'Git', 6)
student_1.rate_lec(lecturer_1 , 'Git', 9)

student_2.rate_lec(lecturer_1 , 'Git', 9)
student_2.rate_lec(lecturer_1 , 'Git', 8)
student_2.rate_lec(lecturer_1 , 'Git', 7)


print (f'Студенты: \n{student_1} \n{student_2}')
print ()
print (f'Лекторы: \n{lecturer_1}')
print ()
print (f'Проверяющие: \n{reviewer_1}')
