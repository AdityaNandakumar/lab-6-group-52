def encode(password):
    password_list = list(password)
    encoded_password = ''
    for i in range(0, len(password_list)):
        new_element = str(int(password_list[i]) + 3)
        encoded_password = encoded_password + new_element[-1]
    return encoded_password


def decode(encoded_password):
    return encoded_password


def main():
    encoded_password_main = ''
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        print('')
        option = int(input('Please enter an option: '))
        if option == 1:
            password_main = input('Please enter your password to encode: ')
            encoded_password_main = encode(password_main)
            print('Your password has been encoded and stored!')
        elif option == 2:
            decoded_password_main = decode(encoded_password_main)
            print('The encoded password is ' + encoded_password_main, end='')
            print(', and the original password is ' + decoded_password_main, end='')
            print('.')
        elif option == 3:
            break


main()

