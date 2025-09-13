# pra declarar funções usamos a palavra chave 'def', de define ou definition provavelmente
# pra criar uma função vazia usa-se 'pass', não pode deixar ela realmente vazia, pois gera erro
# def print_hello():
#     pass
# print_hello()
#-> chamar ela não resulta em nada pois dentro dela só tem o pass

#printar uma função sem o parênteses mostra uma "descrição" dela
# print(print_hello) 
#-> <function print_hello at 0x0000017F28951440>  (basicamente diz q é uma função, o seu nome e o lugar que ela está na memória, mas não executa ela, pra chamar ela precisa dos parênteses)

# def hello_world():
#     print('Hello, world!')

# hello_world() 
#-> Hello, world!
# Função serve basicamente pra reusar código em varias areas sem precisar escrever as mesmas linhas varias vezes, ajuda na manutenção também, pois só é necessário ajustar uma vez ao invés de ajustar em todas partes que iria repetir esse código
# não se repetir no geral é uma coisa boa, é um dos princípios da programação. "DRY" refere-se ao princípio de programação "Don't Repeat Yourself" (Não se repita)

# def return_hello():
#     return 'hello, world!'

# return_hello()
#-> não gera nada pois ela só retorna uma string, a gente precisa fazer algo com isso se quiser algum resultado
# print(return_hello().title().removesuffix('!'))
#-> Hello, World
#como o retorno é string, podemos usar metodos de string nela pra manipular seu resultado

# função com parametro
# def hello_name(nome):
    # a variável 'nome' só interfere dentro dassa função, o escopo dela é essa função. Se em outra parte do código existir uma variável com o mesmo nome, elas não interferem uma com a outra
    #(Python Tutorial: Variable Scope : https://www.youtube.com/watch?v=QVdf0LgmICw)

    # return 'Hello, {}'.format(nome)
#     return f'Hello, {nome.title()}'

# print(hello_name('matheus'))
# chamar essa função sem passar um argumento gera erro, para não gerar precisamos de um valor padrão

# def hello_name2(nome = '"estranho"'):
#     return f'Ola, {nome}'
# print(hello_name2().title())
# print(hello_name2('maTHeuS').title())

# def hello_name3(cumprimento = "Ola", nome = '"estranho"'):
#     return f'{cumprimento}, {nome}'
# print(hello_name3().title())
# print(hello_name3('oI', 'maTHeuS').title())


# *args **kwargs
#    *args: Non-keyword (positional) arguments
#    **kwargs: Keyword arguments
# https://www.geeksforgeeks.org/python/args-kwargs-python/

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# student_info('math', 'art', name = 'john', age=22)
#-> ('math', 'art')   (tuple)
#   {'name': 'john', 'age': 22}   (dictionary)

# courses = ['math', 'art']
# info = {'name' : 'john', 'age':22}

# student_info(courses, info)
#-> (['math', 'art'], {'name': 'john', 'age': 22})
#   {}
# não funcionou de forma correta, passou tudo no args e nada no kwargs. A forma correta de chamar seria 
# student_info(*courses, **info)
#-> ('math', 'art')
#   {'name': 'john', 'age': 22}


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    #  /\ é uma docstring, usada para documentar a funcionalidade de funções, metodos e classes
    # https://www.geeksforgeeks.org/python/python-docstrings/
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2016))

print(days_in_month(2016, 2))