colors = ['Red', 'Yellow', 'Green', 'Orange']

for a in range(0,4):
    print(colors[a])
print(colors[1])
print(colors.append('Blue'))
print(colors.clear())
print(colors.insert(1, 'Indigo'))
print(colors)
print(colors.index('Indigo'))
#print(colors.remove('Indigo'))
print(colors.insert(5, 'Indigo'))

#print(colors.remove('Indigo', 5))
colors.remove(colors[5])
print(len(colors))