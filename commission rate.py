COMMISSION_RATE = 0.10#gobal variable

def showCommission():#showCommission module
        sales = int(input("Enter the amount of sales.: ")): #reading the amount of sales.
        comission = sales * COMMISSION_RATE #calculating commission.
    print("The commission is $",comission) #printing the commission.

keepGoing = "y" #local variable.
while keepGoing == "y" or keepGoing == "Y": #checking the condition is input is y or not.
showCommission() #calling the showCommission.
print("\nDo you want to calculate another.")
keepGoing = str(input("commission?(Enter y for yes): "))#asking the user for calculate another.