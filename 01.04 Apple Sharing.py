x = input("Number of Students: ")
y = input("Number of Apples: ")
numberofstudents = int(x)
numberofapples = int(y)
total = numberofapples // numberofstudents
remainder = numberofapples % numberofstudents
print(total)
print(remainder)