# def thing():
#     print('Hello World!')
#     print('Fun!')
#
# thing()
# print('Zip')
# thing()

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('fr'), 'John')
