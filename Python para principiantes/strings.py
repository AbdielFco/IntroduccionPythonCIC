
myStr = "Hello World"

# Metodos
print(dir(myStr))
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello','bye'))
print(myStr.count('e'))
print(myStr.startswith("Hello"))
print(myStr.endswith("World"))
print(myStr.split())
print(myStr.find('o')) # Posicion
print(len(myStr))
print(myStr.index('e'))
print(myStr[4])

#
print("My name is" + myStr)
print(f"My name is {myStr}")
print("My name is {0}".format(myStr)) 