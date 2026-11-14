
total_classes = 50
classes_attended =int(input("enterclasses attended"))

attendence_percentage = (classes_attended/total_classes)*100
print(attendence_percentage)

if attendence_percentage>=85.0:
    print("your in safe zone")
elif attendence_percentage>=75.0:
     print(" attend the classes regularly")
elif attendence_percentage<75 and attendence_percentage >=66.0:
    print("waring zone")
else:
    medical= input("do you have medical certificate")
    if medical== "yes" and attendence_percentage>=65.0:
     print("can attend thee classes")
    else:
        print("detection alert")  