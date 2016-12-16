#This program calculates the class average for exactly five students. Inputs names too.

import array

print("This program calculates the averages of five students' grades.\n\n")

a_name = raw_input("Insert first student's name: ")
a_grade = input("Insert first student's grade: ")

b_name = raw_input("Insert second student's name: ")
b_grade = input("Insert second student's grade: ")

c_name = raw_input("Insert third student's name: ")
c_grade = input("Insert third student's grade: ")

d_name = raw_input("Insert fourth student's name: ")
d_grade = input("Insert fourth student's grade: ")

e_name = raw_input("Insert fifth student's name: ")
e_grade = input("Insert fifth student's grade: ")

average = ( (a_grade+b_grade+c_grade+d_grade+e_grade) / 5)

print "The class average for the five students is %s." % (average)
