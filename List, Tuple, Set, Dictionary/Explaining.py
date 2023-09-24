# List
a = [1,2,3,4,5,6,7]
print(a)
a.append(8)
a.append(9)
a.append(10)
print(a)
a.insert(0,20)
print(a)
a.pop(0) #Index Value
print(a)

#Tuple
print("Tuple")
a=(1,2,3,4,5,6)
b=list(a)
print(a)
print(b)

#Set
print("Set")
a= {1, 2, 3, 4, 5, 6}
print(a)
a.add(7)
print(a)

#Dictionary
a= {
    "name":"rakesh",
    "age":23,
    "aim":"Developer"
}
print(a)
print(a["name"])
a["age"]=25
a["color"]="red"
print(a)