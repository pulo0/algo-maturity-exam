# Time complexity: O(log n)
def dec_to_other_numeral_system(number:int, base:int):
    if number > 0:
        dec_to_other_numeral_system(number//base, base)
        print('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[number%base], end='')

# Time complexity: O(n)
def num_system_to_dec(number:str, base:int):
    lst = [i for i in number]
    result = 0
    for i in range(len(lst) - 1, -1, -1):
        if lst[i].isdigit():
            result += int(lst[i]) * pow(base, len(lst)-1-i)
        else:
            result += int(ord(lst[i])-55) * pow(base, len(lst)-1-i)
    print(f'\n{result}')

n, b = map(int, input('Select any number you wish to convert and base you want to convert to [2..36]\n').split())
allow_letters_num = input('Select any number you wish to convert (it could be hex symbol like ABCDE)\n').upper()
if n == 0: print('0')
else:
    dec_to_other_numeral_system(n, b)
    num_system_to_dec(allow_letters_num, b)