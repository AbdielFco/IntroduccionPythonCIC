def hello():
    print("HELLO WORLd")

hello()

#
def greeting(name):
    print(f"Hello {name}")

greeting("Juan")

#
def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10,30))

#
sum = lambda numberOne, numberTwo: numberOne + numberTwo
print(sum(10,10))