#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate")
r=float(rate)
pay=0.0
overtime=0.0
if(h>40):
    overtime=(h-40)*1.5*r
    pay=40*r
else:
    pay=h*r
    overtime=0.0
grosspay=pay+overtime
print(grosspay)
    
