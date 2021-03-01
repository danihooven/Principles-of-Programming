""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 06_01

Develop a program that reads students’ grades from a file named “studentdata.txt’,
and writes their names and average into a new file named “studentaverage.txt’.
Round the numbers to the closest integer.



@author: Dani Hooven
@version: 10/13/2020

-------------------------------------------------------------------------------------------------------------------- """
# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

infile = open("studentdata.txt", "r")   # read students' grades
outfile = open("studentaverage.txt", "w")   # write their names and average into a new file

# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM"
# ----------------------------------------------------------------------------------------------------------------------

aline = infile.readline()
while aline:
    values = aline.split()
    count = len(values) - 1
    grades = (values[1:])
    total = sum([int(i) for i in grades])
    average = round(total / count)
    dataline = values[0] + " " + str(average)
    outfile.write(dataline + '\n')
    aline = infile.readline()

infile.close()
outfile.close()