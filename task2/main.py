# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

EXIT_CODE = 'exit'

def isfloat( str ): 
    try:
        float( str )
        return True
    except:
        return False

print( f'For end input list items, press enter or input "{ EXIT_CODE }"' )

data = []

line = None

while line != '' and line != 'exit':
    line = input( 'Input next item: ' )
    if isfloat( line ):
        data.append( float( line ) )
    elif line != EXIT_CODE:
        print( 'Please, input only numbers (press enter or input "exit" for continue)' )

print( f'You input: { data }' )

for i in range( len( data ) ):
    if i % 2 == 1:
        data[i - 1], data[i] = data[i], data[i - 1]

print( f'Swap list: { data }')
