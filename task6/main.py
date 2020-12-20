# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
# единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у
# пользователя.
#
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика
# товара, например название, а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
#
# {
#   “название”: [“компьютер”, “принтер”, “сканер”],
#   “цена”: [20000, 6000, 2000],
#   “количество”: [5, 2, 7],
#   “ед”: [“шт.”]
# }


#
# Input helpers
#

# Check float
def isfloat( val ):
    try:
        float( val )
        return True
    except:
        return False

# Input not empty string wrapper
def inputNotEmptyString( title ):
    result = input( f"{ title } (not empty string): " )
    result = result.strip()
    if not result:
        raise Exception( f"{ title } is empty" )
    return result

# Input positive float wrapper
def inputPositiveFloat( title ):
    result = input( f"{ title } (positive number): ")
    if not isfloat( result ):
        raise Exception( f"{ title } is not number")
    result = float( result )
    if result <= 0:
        raise Exception( f"{ title } is not positive number" )
    return result

# Input positive integer wrapper
def inputPositiveInt( title ):
    result = input( f"{ title } (positive integer): " )
    if not result.isnumeric():
        raise Exception( f"{ title } is not integer number" )
    result = int( result )
    if result <= 0:
        raise Exception( f"{ title } is not positive integer number" )
    return result

#
# Program
#

# Product store
def productsStore():
    products = []

    def analizate():
        if len( products ) == 0:
            return {}

        chars = [ ch for id, ch in products ]

        values = list( zip( *[ list( ch.values() ) for ch in chars ] ) )

        result = { key: list( set( values[i] ) ) for i, key in enumerate( chars[0].keys() ) }

        return result

    return {
        'add': lambda product: products.append( product ),
        'analizate': analizate,
        'print': lambda : print( products )
    }

# Product reader
def readProduct():
    print( "Input product info" )
    return ( 
        inputPositiveInt( "Input product code" ),
        {
            "name":  inputNotEmptyString( "Input product name" ),
            "price": inputPositiveFloat( "Input product price" ),
            "count": inputPositiveFloat( "Input product count" ),
            "unit":  inputNotEmptyString( "Input product unit")
        }
    )

store = productsStore()

# Simple menu
while True:
    print (
        "Select menu item:\n" \
        "1. Print products\n" \
        "2. Add product\n" \
        "3. Analizte products\n" \
        "0. Exit\n"
    )
    cmd = -1

    try:
        cmd = int( input( "Cmd: " ) )
    except:
        print( "Invalid menu item" )

    if cmd == 0:
        exit()
    elif cmd == 1:
        store['print']()
    elif cmd == 2:
        try:
            product = readProduct()
            store['add']( product )
            print( f"Product add success: {product}")
        except Exception as ex:
            print( "Invalid product data: ", ex )
    elif cmd == 3:
        print( f"Analize: {store['analizate']()}" )
    else:
        print( f"Unknown command: {cmd}" )
    print( "-----------------------------\n" )



