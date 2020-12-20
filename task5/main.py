# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

# Float validator
def isfloat( s ):
    try:
        float( s )
        return True
    except:
        return False

# Raiting help function
def reiting( default = [] ):
    head = {
        'value': None,
        'next': None
    }

    def toString():
        if head['value'] is None:
            return '[]'
        
        result = '[ '
        current = head
        
        while current is not None:
            result = result + str( current['value'] )
            if current['next'] is not None:
                result = result + ' -> '
            current = current['next']
        
        return result + ' ]'


    def add( value, prev, next ):
        # It`s possible only if next is head
        if prev is None:
            if next['value'] is None or next['value'] < value:
                head['next'] = None if next['value'] is None else next.copy()
                head['value'] = value
            else:
                add( value, next, next['next'] )
        # It`s possible only if next is tail
        elif next is None:
            prev['next'] = {
                'value': value,
                'next': None
            }
        # Ordinary situation ( prev >= value > next )
        elif prev['value'] >= value and next['value'] < value:
            n = {
                'value': value,
                'next': next.copy()
            }
            prev['next'] = n
        # So, go next...
        else:
            add( value, next, next['next'] )

    for item in default:
        add( item, None, head )

    return {
        'toString': toString,
        'add': lambda value: add( value, None, head ),
    }

r = reiting( [3, 2, 1, 8] )

EXIT_CODE = 'exit'
line = None

print( f'Initial value: { r["toString"]() }' )

print( 'Enter number for raiting struct. Press enter or input "exit" for exit.' )

while line != '' and line != EXIT_CODE:
    line = input( 'Input number: ' )
    if isfloat( line ):
        r['add']( float( line ) )
        print( r['toString']() )
        print( '------------------------' )
    elif line != '' and line != EXIT_CODE:
        print( 'Please, input number (press enter or input "exit" for exit)' )
