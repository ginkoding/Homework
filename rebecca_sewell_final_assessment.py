# """
# TASK 1

# Design a parent class called CFGStudent.

# It should have general attributes like name, surname, age, email, student id
# and methods to fetch student's full name and student's id.

# Design a child class called NanoStudent, which  inherits from CFGStudent class.
# This class should have exactly the same attributes as its parent class,
# as well as an additional one called 'specialization' and course grades.

# The child class 'generate_id' method should override its parent method to add the suffix 'NANO'
# in front of the id.

# New methods 'add_new_grade' and 'get_course_grades' should be added.
# You can use  it as a skeleton code for your classes OR adjust it and create your own.

# SEE NOTES BELOW

# """
# import random


# class CFGStudent:

#     def __init__(self, name, surname, age, email, student_id):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.email = email
#         self.student_id = student_id

#     @staticmethod
#     def generate_id():
#         student_id = random.randint(1000, 10000)
#         return student_id({})

#     def get_id(self):
#         print(self.student_id)

#     def get_fullname(self):
#         print(name, surname):


# class NanoStudent(CFGStudent):

#     def __init__(self, specialization1, grades):
#         self.specialization = specialization1
#         self.course_grades = grades

#     @staticmethod
#     def generate_id():
#         student_id = random.randint(1000, 10000)
#         return (("NANO")+student_id({}))

#     def add_new_grade(self, new_grade):
#         self.grades.append(new_grade)

#     def get_course_grades(self):
#         return self.grades


# ############################################

# # Example run

# # do not pass ID, it should be generated automatically
# s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')
# print(s.get_fullname())
# # returns 'Anna Smith'
# print(s.student_id)
# # returns '3868' or some other random number

# cfg_s = NanoStudent('Software', name='Mia',
#                     surname='Papandopulu', age=20, email='mia@mail.com')
# print(cfg_s.get_fullname())
# # returns 'Mia Papandopulu'
# print(cfg_s.get_id())
# # returns 'NANO6180' or some other random number

# cfg_s.add_new_grade('theory', 95)
# cfg_s.add_new_grade('project', 78)
# print(cfg_s.get_course_grades())
# # returns {'theory': 95, 'project': 78}


"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence
and return the sum of all even Fibonacci numbers. See more details in the task description in
your assessment paper.
"""


def fib(n):

    if n == 1 or n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


n = 10
sum =
for i in range(0, n):
    even_fibonacci_sum = fib(i)
    sum += even_fibonacci_sum

    ##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0


"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution.
"""


def is_valid_subsequence(array, sequence):
    j = 0
    for val in array:
        if j == len(sequence):
            break
        if sequence[j] == val:
            j += 1
    return j == len(sequence)

#### TESTS ####


array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, -2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence2 = [1, 6, -1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE


"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""


"""
The code could be improved by following the DRY method, not needing to repeat the employee
information. There is a lot of repetition in the code which could be avoided.

They could leave comments for other developers to use, or in case they come 
back to the code in several months time. 

They did avoide camelCase in their function naming, which follows Python recommended guidelines
by using underscores to sperate words. 






"""
