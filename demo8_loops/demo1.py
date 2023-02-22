#print 1 to 10

# for i in range(1,11):
#     print(i)
# for i in range(1,11,3):
#     print
#
# colors = ['Red', 'Yellow', 'Green', 'Orange']
# #sprint(len(colors))
# for a in range(0,len(colors)):
#     print(colors[a])

numbers=[45,98,75,65,24,88,74,56,75]
numbers1=[]
for a in range(0, len(numbers)):
    print(numbers[a])

    if numbers[a] <= 50:
        numbers1.append(numbers[a])

print(numbers1)