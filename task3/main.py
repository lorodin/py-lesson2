# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

def inputMounth():
    try:
        mounth = int( input( 'Mounth number [1...12]:' ) )
        if mounth > 0 and mounth < 13:
            return mounth
        raise Exception()
    except:
        print( 'Incorrect mounth number' )
        exit()

mounth = inputMounth()

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {
    'winter': [1, 2, 12],
    'spring': [3, 4, 5],
    'summer': [6, 7 , 8],
    'autumn': [9, 10, 11]
}

#####################################################
#          No:  1  2  3  4  5  6  7  8  9 10 11 12  #
#     No // 3:  0  0  1  1  1  2  2  2  3  3  3  4  #
# No // 3 % 4:  0  0  1  1  1  2  2  2  3  3  3  0  #
#####################################################
list_index = mounth // 3 % 4

print( f"Season from list: { seasons_list[list_index] }" )

for season, mounthes in seasons_dict.items():
    if mounthes.count( mounth ):
        print( f"Season from dict: { season }" )
        break