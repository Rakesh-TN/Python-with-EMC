salaries = int(input("Enter the Salary : "))
age = int(input("Enter the Age : "))
if (salaries>=20000 or age<=25):
    loan = int(input("Loan : "))
    if (loan>50000):
        print("Maximum loan amount is 50000")
    else:
        print("You're Eligible for Loan")
else:
    print("You're Eligible for Loan")