a = int(input("A :"))
b = int(input("B :"))
Operation = input("+,-,*,/ :")
if (Operation=="+"):
    print(a+b)
elif (Operation=="-"):
    print(a-b)
elif (Operation=="*"):
    print(a*b)
elif (Operation=="/"):
    print(a/b)
else:
    print(Operation,"is Invalid Operator")