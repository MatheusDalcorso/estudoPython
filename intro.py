# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

# Floor division is a division operation that returns the largest integer 
# that is less than or equal to the result of the division.
# In Python, it is denoted by the double forward slash '//'. 

# number = 1

# print(type(number))

# print(round(3.1415, 2))

# num1 = '100'
# num2 = '200'
# num1 = int(num1)
# num2 = int(num2)
# print(num1 + num2)

# courses = ['history', 'math', 'phisics', 'compSci']
#print(len(courses))

# courses.append('art')

#insert leva 2 argumentos, o index onde o valor será inserido e o valor a ser inserido

# courses.insert(0,'portuguese')


# courses_2 = ['geography', 'physicalEd']

# courses.extend(courses_2)

# .remove(valor) é usado para remover o valor da lista
# courses.remove('math')
#.pop() é usado para remover o ultimo valor da lista. Uma coisa legal dele é que ele retorna o valor que removeu da lista, então você pode pegar esse valor para usar em outra coisa
#popped = courses.pop()

#courses.reverse()
# numList = [50, 84, 37, 5, 0]
#numList.sort(reverse=True)
# numListOrganizada = sorted(numList)

#print(courses[-4])
#print(courses[0:])
#print(sum(numList))
#print(numListOrganizada)

#print(courses.index('compSci'))

#print('math' in courses)


#loop pra printar todos os itens da lista courses
# for course in courses:
#     print(course)

# for index, course in enumerate(courses, start=3):
#     print(index, course)

# courses_str = ' - '.join(courses)

# new_list = courses_str.split(' - ')

# print(new_list)

# print(courses_str)





# Mutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_2[0] = 'Art'

# print(tuple_1)
# print(tuple_2)
# print(tuple_1[0])





# Sets
# cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
# other_courses = {'Math', 'geography', 'physicalEd', 'portuguese'}

# print(cs_courses.intersection(other_courses))
# print(cs_courses.difference(other_courses))
# print(cs_courses.union(other_courses))





# # Empty Lists
# empty_list = []
# empty_list = list()

# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty Sets
# empty_set = {} # Não podemos usar assim. Isso não é um set vazio, é um dictionary vazio
# empty_set = set()





message = "Hello, world!"
courses = ['history', 'math', 'phisics', 'compSci']

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# student = {'name': 'John', 'age': 25, 'courses': courses}

# print(student)

# print(student['name'])
# print(student['age'])
# print(student['courses'])
# print(student['courses'][0])
# print(student['courses'][1])

# print(student.get('name'))
# print(student.get('phone'))
# print(student.get('name', 'No key found'))
# print(student.get('phone', courses))

student['phone'] = '3625-3625'

# print(student.get('phone', 'No key found'))


# student['name'] = 'Matt'
student.update({'name': 'Lucas', 'age': '30', 'id': '1'})

# print(student)


del student['id']

# print(student)

phone = student.pop('phone')
# print(student)
# print(phone)



# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())

# for key in student.items():
#     print(type(key))

for key, value in student.items():
    print(key, value)


