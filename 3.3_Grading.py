'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
semgrade = input("What was your semester grade? ")
finalgrade = input("What was your Final Exam grade? ")
weight = input("What is the weight of the exam? (ex: 20% would be 20) ")

semweight = (100 - int(weight)) * 0.01
semweightgrade = int(semgrade) * semweight

finalweightgrade = int(finalgrade) * int(weight) *0.01

overall = semweightgrade + finalweightgrade
overall = round(overall,1)
print ("Your overall grade is " +str(overall))