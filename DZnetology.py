class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.course_grades:
                    lecturer.course_grades[course] += [grade]
                else:
                    lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка1'

    def __average_hw_grade(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.__average_hw_grade() < other.__average_hw_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.__average_hw_grade() > other.__average_hw_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.__average_hw_grade() == other.__average_hw_grade()

    def __str__(self):
        average = self.__average_hw_grade()
        some_student = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашние задания: {round(average)}\n' f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}
        Lecturer.lecturer_list.append(self)

    def __average_lecture_grade(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.course_grades:
            grades_count += len(self.course_grades[grade])
            grades_sum += sum(self.course_grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваются объекты разных классов')
            return
        return self.__average_lecture_grade() < other.__average_lecture_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваются объекты разных классов')
            return
        return self.__average_lecture_grade() > other.__average_lecture_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваются объекты разных классов')
            return
        return self.__average_lecture_grade() == other.__average_lecture_grade()

    def __str__(self):
        mean_grade = self.__average_lecture_grade()
        some_lecturer = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {round(mean_grade, 1)}\n'
        return some_lecturer


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка4'

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'
        return some_reviewer


best_student = Student('Ванька', 'Встанька', 'M')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

best_student1 = Student('Петя', 'Петров', 'M')
best_student1.courses_in_progress += ['Python', 'Git']
best_student1.finished_courses += ['Введение в программирование']
students_list = [best_student, best_student1]

cool_lecturer = Lecturer('Паша', 'Пашкевич')
cool_lecturer.courses_attached += ['Python']

cool_lecturer1 = Lecturer('Вася', 'Пупкин')
cool_lecturer1.courses_attached += ['Python']
lecturer_list = [cool_lecturer, cool_lecturer1]

cool_reviewer = Reviewer('Паша', 'Пашкевич')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(best_student1, 'Python', 5)
cool_reviewer.rate_hw(best_student1, 'Python', 8)
cool_reviewer.rate_hw(best_student1, 'Python', 5)

best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 9)
best_student.rate_lect(cool_lecturer, 'Python', 8)

best_student.rate_lect(cool_lecturer1, 'Python', 7)
best_student.rate_lect(cool_lecturer1, 'Python', 8)
best_student.rate_lect(cool_lecturer1, 'Python', 9)

print(cool_reviewer)
print(cool_lecturer)
print(cool_lecturer1)
print(best_student)
print(best_student1)


def grades_students(students_list, course):
    overall_student_rating = 0
    lectors = 0
    for listener in students_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(listener.grades[course])
            average_student_score += overall_student_rating
            lectors += 1
    if overall_student_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{round(overall_student_rating / lectors, 1)}'


def grades_lecturers(lecturer_list, course):
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.course_grades.keys():
            lecturer_average_rates = 0
            for rate in lecturer.course_grades[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.course_grades[course])
            average_rating += overall_lecturer_average_rates
            b += 1
    if average_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{round(average_rating / b, 1)}'


if best_student < best_student1:
    print(f'Средняя оценка {best_student.name} {best_student.surname} меньше, чем средняя оценка {best_student1.name} {best_student1.surname}')
elif best_student > best_student1:
    print(f'Средняя оценка {best_student.name} {best_student.surname} больше, чем средняя оценка {best_student1.name} {best_student1.surname}')
else:
    print(f'Средняя оценка {best_student.name} {best_student.surname}  равна средней оценке {best_student1.name} {best_student1.surname}')
print()

if cool_lecturer > cool_lecturer1:
    print(f'Средняя оценка {cool_lecturer.name} {cool_lecturer.surname} больше, чем средняя оценка {cool_lecturer1.name} {cool_lecturer1.surname}')
elif cool_lecturer < cool_lecturer1:
    print(f'Средняя оценка {cool_lecturer.name} {cool_lecturer.surname} меньше, чем средняя оценка {cool_lecturer1.name} {cool_lecturer1.surname}')
else:
    print(f'Средняя оценка {cool_lecturer.name} {cool_lecturer.surname}  равна средней оценке {cool_lecturer1.name} {cool_lecturer1.surname}')
print()

print(f'Средняя оценка студентов по курсу "Python": {grades_students(students_list, "Python")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lecturer_list, "Python")}')