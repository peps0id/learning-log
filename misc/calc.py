print("summ, sub, divide, mult")
interaction = input("which one do you wan't to use? ")
x = float(input("first variable "))
y = float(input("second variable "))
if interaction == ("summ"):
    print(x+y)
elif interaction == ("sub"):
    print(x-y)
elif interaction == ("divide"):
    print(x/y)
else: print(x * y)