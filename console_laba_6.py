from getpass import getpass
from time import sleep


def function():
    name = input('Enter your name: ')
    password = getpass('Enter password: ')
    if name and password:
        rep_pass = getpass('Repeat pass: ')

        counter = 3
        while password != rep_pass:
            print('Pass error...')
            counter -= 1
            rep_pass = getpass(f'Left to try {counter} ->')

            if counter == 1:
                print('ARE YOU BLOCKED!')
                break
            print('welcome!')
    else:
        print('Incorrect data...')


def main():
    function()


if __name__ == '__main__':
    main()