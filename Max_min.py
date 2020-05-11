"""
a program that repeatedly prompts a user for integer numbers until the user enters "done". 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except 
and put out an appropriate message and ignore the number.
"""
def done(largest,smallest):
    try:
        max=int(largest)
        min=int(smallest)
        print("Maximum is",max)
        print("Minimum is",min)
    except:
        print("enter atleast one number")

largest = 0
smallest = None
while True:
    userInp = input("Enter a number: ")
    if (userInp == "done"):
        break
    try:
        num = float(userInp)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num
done(largest,smallest)
