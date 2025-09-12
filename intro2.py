# if True:
#     print("Condição True")

# if False:
#     print("Condição True")



# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is (https://www.w3schools.com/python/ref_keyword_is.asp)
#                   \/
# The 'is' keyword is used to test if two variables refer to the same object.
# The test returns True if the two objects are the same object.
# The test returns False if they are not the same object, even if the two objects are 100% equal.
# Use the == operator to test if two variables are equal.

# language = "  PyTHON   "
# language = "  JAva   "
# language = "C"


# if e elif
# if language.lower().strip() == "python":
#     print("Linguagem é python")
# elif language.lower().strip() == "java":
#     print("Linguagem é java")
# else:
#     print("Sem resultados")

# Python não possui switch case


# Além dessas comparações que coloquei acima, tamém temos operações booleanas que podemos usar
# Elas são: and (&&), or (||) e not (!)

# user = 'admin'
# logged_in = False

# if user == 'admin' or logged_in:
#     print('Página do Admin')
# else:
#     print('Acesso negado')

# if user == 'admin' and not (not logged_in):
#     print('Página do Admin')
# else:
#     print('Acesso negado')


# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a
# print("a = [1, 2, 3]\nb = [1, 2, 3]\nc = a")
# print('')
# print('Teste com "b"')
# print(f"a == b : {a == b}")
# print(f"a is b : {a is b}")
# print(f"id 'a': {id(a)} \nid 'b': {id(b)}")
# print('')
# print('Teste com "c"')
# print(f"a == c : {a == c}")
# print(f"a is c : {a is c}")
# print(f"id 'a': {id(a)} \nid 'c': {id(c)}")

# a comparação com is funciona basicamente como id(variavel1) == id(variavel2)


# False Values:
    # False
    # None     (Python does not have a literal 'null' keyword. None é basicamente o null de python)
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.    
# (A mapping is a collection that allows you to look up a key and retrieve its value. https://realpython.com/python-mappings/)

# Todo resto é True

condition = [""]

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#exemplo de uso, preciso checar alguma função retornou uma string com valores
string = ''

if string:
    print('String com algum valor')
else:
    print('String vazia')
 








