demo_list = [1,'hello',1.34,True,[1,2,3]]
colors = ['red','green','blue']

number_list = list((1,2,3,4))
print(number_list)

#
r = list(range(1,10))
print(r)

#
print(dir(colors))
print(len(demo_list))
print(colors[1])
print('green' in colors)

#
colors[1] = "yellow"
print(colors)

#
colors.append('violet')
print(colors)

#
colors.extend(['black','white'])
print(colors)

#
colors.insert(0,'gray')
print(colors)

#
colors.pop()
print(colors)

#
colors.pop(0)
print(colors)

#
colors.remove('red')
print(colors)

#
# colors.clear()
# print(colors)

#
colors.sort(reverse=True)
print(colors)
