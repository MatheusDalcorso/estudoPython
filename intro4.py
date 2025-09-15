import sys
# sys.path.append('C:\\Users\\Mathe\\OneDrive\\Desktop\\teste')

# pra importar o modulo, e apelidar de fm (apelido é opcional mas útil)
import first_module as fm

courses = ['history', 'math', 'physics', 'compsci']

index = fm.find_index(courses, 'physics')
# pra usar uma função de um modulo importado precisamos digitar o nome do modulo primeiro e depois o que queremos usar daquele modulo
# print(index) # -> 2 (passando 'physics' no argumento)

# print(fm.test)
# a variavel teste também é importada, e igual a função, ela precisa ser chamada referenciando o modulo

# ficar referenciando o nome do modulo pode ficar meio comprido dependendo do nome, então podemos dar um apelido escrevendo na frente da importação (de import first_module -> import first_module as fm) parece com o apelido das tabelas em sql
#assim podemos usar somente fm para referenciar ele (index = fm.find_index(courses, 'physics'))

# pra importar a função
from first_module import find_index as fi, test #as t
# importando a função não é necessario referenciar de onde ela veio
# mas só da acesso a essa função e o que você importar nada mais do modulo
# também podemos apelidar a função da mesma maneira que apelidamos o modulo
# de maneira geral é bom deixar o nome da variavel de uma maneira facil de ler, 'fi' não facilita a leitura então pode não ser a melhor opção
 
# index = find_index(courses, 'compsci')
index = fi(courses, 'compsci')
# print(index)

# from first_module import *
# importa tudo do modulo. Não é visto como uma boa prática por vários motivos como poluir seu namespace, pode ficar difícil saber de onde vem uma função especifica, risco de sobreescrever uma variavel/função e etc
# https://www.geeksforgeeks.org/python/why-import-star-in-python-is-a-bad-idea/


# como o python sabe como encontrar o modulo first_module?
# quando a gente importa um módulo ele checa alguns lugares, podemos saber quais lugares importando 'sys' e vendo o .path
#import sys

#print(sys.path)
# ['c:\\estudoPython',
#  'C:\\Users\\Mathe\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip',
#  'C:\\Users\\Mathe\\AppData\\Local\\Programs\\Python\\Python313\\DLLs',
#  'C:\\Users\\Mathe\\AppData\\Local\\Programs\\Python\\Python313\\Lib',
#  'C:\\Users\\Mathe\\AppData\\Local\\Programs\\Python\\Python313',
#  'C:\\Users\\Mathe\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']


# esses são os lugares que o python olha pra procurar o modulo quando eu importo eles
#quais diretórios são adicionados nessa lista? primeiro é o local do arquivo que estamos rodando, depois ele adiciona os diretoris listados na variável de ambiente PYTHONPATH, depois os diretórios de biblioteca padrões (por isso podemos adicionar os modulos padrões) e por ultimo olha no diretório de pacotes de site por pacotes de terceiros
# (https://www.geeksforgeeks.org/python/sys-path-in-python/)

# ao esconder o arquivo first_module.py em uma pasta na area de trabalho e rodar o código, recebemos esse erro
# Traceback (most recent call last):
#   File "c:\estudoPython\intro4.py", line 2, in <module>
#     import first_module as fm
# ModuleNotFoundError: No module named 'first_module'

# Tem algumas coisas que podemos fazer para lidar com isso
# Nós podemos adicionar o diretório no nosso sys.path com append
# sys.path.append('C:\\Users\\Mathe\\OneDrive\\Desktop\\teste')

# não é a melhor solução, é preferivel mudar na variável de ambiente PYTHONPATH 
# pra ver como siga esse video https://www.youtube.com/watch?v=CqvZ3vGoGs0&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=11&t=702s


# usar módulos das bibilioteca padrão é uma boa ideia, afinal não tem porque reinventar a roda, aqueles modulos são usados e aprovados a anos. Não tem problema tentar escrever um código seu, mas para resolver um problema que já tem a resposta é sempre bom usar o recurso disponível

import random

random_course = random.choice(courses)

print(random_course) #-> imprime um valor randomico da variavel courses