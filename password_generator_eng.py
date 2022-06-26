import random

name = input('Enter your name, please --> ')

print(f'Hello {name}! This program is designed to generate strong passwords.')



digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''                                                                                        #in this variable we add the necessary symbols

number_of_passwords = int(input('Enter the number of passwords to generate --> '))
length = int(input('Enter length of passwords --> '))

need_digits = input('Include digits in password? yes/no --> ')
if need_digits.lower() == 'yes':
    chars += digits

need_uppercase_letters = input('Include uppercase letters in password? yes/no --> ')
if need_uppercase_letters.lower() == 'yes':
    chars += uppercase_letters

need_lowercase_letters = input('Include lowercase letters in password? yes/no --> ')
if need_lowercase_letters.lower() == 'yes':
    chars += lowercase_letters

need_punctuation = input('Include the symbols "!#$%&*+-=?@^_"? yes/no --> ')
if need_punctuation.lower() == 'yes':
    chars += punctuation

need_no_simbols = input('Exclude the ambiguous symbols "il1Lo0O"? yes/no --> ')
if need_no_simbols.lower() == 'yes':                                                               #delete these symbols
    need_no_simbols = need_no_simbols.replace('i', '')
    need_no_simbols = need_no_simbols.replace('l', '')
    need_no_simbols = need_no_simbols.replace('1', '')
    need_no_simbols = need_no_simbols.replace('L', '')
    need_no_simbols = need_no_simbols.replace('o', '')
    need_no_simbols = need_no_simbols.replace('0', '')
    need_no_simbols = need_no_simbols.replace('O', '')

print()

chars = list(chars)                                                                                #convert string variable to list


def generate_password(length, chars):
    password = random.sample(chars, length)
    return password

for i in range(number_of_passwords):
    print(*generate_password(length, chars), sep='')

print()

for_exit = input('Press anything to exit ')
