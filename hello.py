#cria variável
message = "Hello, world!"

#string de multiplas linhas
#message = """Hello,



#world!"""

#message = "matheus's world"
#message = 'matheus\'s world'

#message = 'matheus"s world'
#message = "matheus\"s world"

# Print hello world
#print(message)

#printa o numero de chars da string
#print(len(message))

#printa o char da posição, tratando a string como um array
#print(message[12])
#tentar acessar uma posição inexistente gera erro, 
# diferente do c que deixa e volta um valor alocado naquele espaço de memoria

#printa do espaço 0 até o 5, mas não incluindo o 5
#print(message[0:5])
#print(message[:5])
#print(message[7:13])
#print(message[7:])

# Print hello world, mas o .lower() deixa tudo em minusculo
#print(message.lower())

# Print hello world, mas o .upper() deixa tudo em maiusculo
#print(message.upper())

#.count(argumento) conta o numero de vezes que aparece o argumento, no caso de 'Hello', aparece 1
#.count('l') ele printa 3, pois aparecem 3 vezes
#print(message.count('l'))

# .find(argumento) vai printar onde começa oque vc quer achar, no caso de Hello ele mostra 0
#no caso de world ele mostra 7
#se o argumento não existir ele mostra -1
#se tiver mais q um ele mostra a posição do primeiro, com l ele mostra 2
#print(message.find('l'))


#.replace(argumento_a_ser_substituido, argumento_substituto)
# no caso de baixo ele troca world por universe, mas esse retorno precisa ir para uma variavel
# só fazer message.replace('world', 'universe') não funciona para o print abaixo
# new_message = message.replace('world', 'universe')
# message = message.replace('world', 'universe')

# print(message)

# print(new_message)

# greeting = "Hello"
# name = "Matheus"

# message = greeting + ', ' + name + '. Welcome!'

# messageFormat = '{}, {}. Welcome!'.format(greeting, name)

# messageFString = f'{greeting}, {name.upper()}. Welcome!'

# print(message)
# print(messageFormat)
# print(messageFString)

#print(dir(message))

help(str.upper)


