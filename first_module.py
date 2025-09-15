print('Imported first_module.')
# Print mostra toda vez que rodarmos o aquivo que importou o modulo, então quando rodar o intro4 vai printar a mensagem na tela
test = 'Test String'

def find_index(to_search, target):
    '''Find the index of the value in a sequence'''
    
    for i, value in enumerate(to_search):
                    # The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object. The enumerate() function adds a counter as the key of the enumerate object.
        if value == target:
            return i
    
    return -1