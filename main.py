import os
import test as t
import test2 as t2

def print_line(msg):
    print(f'Alert: {msg}')

def main():
    print('====== Main ======')
    print_line('This is the beginning.')
    t.guess_odd()
    print_line('This is the end.')
if __name__ == '__main__':
    main()
