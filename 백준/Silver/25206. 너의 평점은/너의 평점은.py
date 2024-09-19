n = 1
totalTime = 0
totalGrade = 0
while n <= 20:
    Sub, Time, Grade = map(str, input().split())
    n += 1
    if Grade == "P":
        pass
    elif Grade == "A+":
        totalGrade += 4.5*float(Time)
        totalTime += float(Time)
    elif Grade == "A0":
        totalGrade += 4.0*float(Time)
        totalTime += float(Time)
    elif Grade == "B+":
        totalGrade += 3.5*float(Time)
        totalTime += float(Time)
    elif Grade == "B0":
        totalGrade += 3.0*float(Time)
        totalTime += float(Time)
    elif Grade == "C+":
        totalGrade += 2.5*float(Time)
        totalTime += float(Time)
    elif Grade == "C0":
        totalGrade += 2.0*float(Time)
        totalTime += float(Time)
    elif Grade == "D+":
        totalGrade += 1.5*float(Time)
        totalTime += float(Time)
    elif Grade == "D0":
        totalGrade += 1.0*float(Time)
        totalTime += float(Time)
    elif Grade == "F":
        totalGrade += 0.0*float(Time)
        totalTime += float(Time)

print(totalGrade/totalTime)