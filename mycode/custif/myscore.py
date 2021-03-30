#!/usr/bin/env python3

message = 'Your grade calculation: '

# wrap connection in a float() to accept decimals as numbers
examscore = float(input("What was your exam grade??\n"))

# if input value is between...
if examscore >= 0 and examscore < 60:
    message = message + 'Exam score is an F.\nDUDE, COME ON!!!'
elif examscore >= 60 and examscore < 70:
    message = message + 'Exam score is a D.\n MUST. TRY. HARDER.'
elif examscore >= 70 and examscore < 80:
    message = message + 'Exam score is a C.\nDUDE, STOP SLACKING OFF.'
elif examscore >= 80 and examscore < 90:
    message = message + 'Exam score is a B.\nNOT TOO SHABBY!'
elif examscore >= 90 and examscore <=100:
    message = message + 'Exam score is an A.\nEASY! EASY! EASY!'
else:
    message = message + 'exam score was an invalid number.'
print(message)

