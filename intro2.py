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

user = 'admin'
logged_in = False

if user == 'admin' and (not logged_in):
    print('Página do Admin')
else:
    print('Acesso negado')


