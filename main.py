student_list = []
lecturer_list = []


class Student:

    def __init__(self, name, surname, gender):
        student_list.append(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.av_grade = []

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        sum_ = 0
        len_ = 0
        for v in self.grades.values():
            for i in v:
                sum_ += i
                len_ += 1
                self.av_grade = round(sum_ / len_, 1)
        return self.av_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return self.av_grade < other.av_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСреднняя оценка за домашнее задание: {self._average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        lecturer_list.append(self)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'
        return res

    def _average_grade(self):
        sum_ = 0
        len_ = 0
        for v in self.grades.values():
            for i in v:
                sum_ += i
                len_ += 1
                self.av_grade = round(sum_ / len_, 1)
        return self.av_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a student')
            return
        return self.av_grade < other.av_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создаем студентов
student_1 = Student('Ivanov', 'Ivan', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Petrov', 'Petr', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

# Создаем лекторов
lecturer_1 = Lecturer('Alexeev', 'Alexey')
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2 = Lecturer('Fedorov', 'Fedor')
lecturer_2.courses_attached += ['Git', 'Python']

# Создаем экспертов
reviewer_1 = Reviewer('Sergeev', 'Sergey')
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2 = Reviewer('Aleksandrov', 'Aleksandr')
reviewer_2.courses_attached += ['Git', 'Python']

# Ставим оценки лекторам
student_1.rate_lc(lecturer_1, 'Python', 9)
student_1.rate_lc(lecturer_1, 'Git', 7)
student_1.rate_lc(lecturer_2, 'Python', 8)
student_1.rate_lc(lecturer_2, 'Git', 7)
student_2.rate_lc(lecturer_1, 'Python', 6)
student_2.rate_lc(lecturer_2, 'Git', 6)
student_2.rate_lc(lecturer_1, 'Python', 5)
student_2.rate_lc(lecturer_2, 'Git', 10)

# Ставим оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Git', 6)


print(student_1.__str__())
print(student_2.__str__())
print(lecturer_1.__str__())
print(lecturer_2.__str__())
print(student_1 > student_2)
print(lecturer_1 < lecturer_2)


def average_grade_hw_in_course(stud_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in stud_list:
        if course_name in stud.courses_in_progress:
            count_all += 1
            for course, grade in stud.grades.items():
                if course == course_name:
                    for v in grade:
                        sum_all += v
                        return f'Средняя оценка студентов на курсе {course_name} - {sum_all / count_all}'


def average_grade_lc_in_course(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if course_name in lect.courses_attached:
            count_all += 1
            for course, grade in lect.grades.items():
                if course == course_name:
                    for v in grade:
                        sum_all += v
                        return f'Срендняя оценка лекторов на курсе {course_name} - {sum_all / count_all}'


print(average_grade_hw_in_course(student_list, 'Python'))
print(average_grade_hw_in_course(student_list, 'Git'))
print(average_grade_lc_in_course(lecturer_list, 'Python'))
print(average_grade_lc_in_course(lecturer_list, 'Git'))