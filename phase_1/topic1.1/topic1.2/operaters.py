food = float(input ("enter the food amount "))
gst_per=float(input ("enter the GST"))
delivery= float(input("enter the delivery charges "))
frnds =int(input("number of friends"))

gst = food*gst_per/100
print(gst)
total = food+gst+delivery
print(total)
share= total/frnds
print(share)