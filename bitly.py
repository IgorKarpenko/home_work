import random

urls = {}

symbols = 'A,D,F,G,d,R,E,T,Y,U,I,O'.split(',')

def generate_code():
    number_of_symbols = 7
    code = ''.join(random.choice(symbols) for i in range(7))
    return code # составить строку из 7 случайных символов
# ДОПОЛНИТЬ ----------------


def add_to_urls(code):
    url = input('Введите ссылку:')
    if code not in urls:
        urls.update({code:url})
    else:
        urls.update({generate_code():url})
    
def get_by_code(code):
    if urls.get(code) != None:
        return print(urls.get(code))
    else:
        print('The web-page with this key was not found')



add_to_urls('AAAAAAA')
