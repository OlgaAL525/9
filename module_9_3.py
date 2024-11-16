first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = list(zip(first, second))

first_result = (len(x[0]) - len(x[1]) for x in zp if len(x[0]) != len(x[1]))
a = list()
for i in first_result:
   a.append(i)
print(a)

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
b = list()
for i in second_result:
   b.append(i)
print(b)
