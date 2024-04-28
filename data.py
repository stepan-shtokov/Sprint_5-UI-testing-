from random import randint


class User:
    user_name = 'Степан'
    email = 'stepan.shtokov_8_123@gmail.com'
    password = 'q153698742Q'


class RandomUser:
    user_name = f'TestName{randint(0, 999)}'
    email = f'mailtest{randint(0, 999)}@gmail.com'
    password = f'qw{randint(1000, 9999)}rty'
