from random import randint

def generate_num():
    return randint(1, 3)

def guess_odd():
    print('[Guess Number Game]')
    print('Let\'s guess!')
    num = generate_num()
    if num % 2 == 1:
        print(f'{num}: This is an odd number.')
    else:
        print(f'{num}: This is an even number.')

def print_result():
    print('test')