from googletrans import Translator, LANGUAGES

title = 'test'
text = 'test'
author = 'test'
date = '13.02.2026'

data = f'{title} {text} {author} {date}'


print(f'выберите доступный язык:')

for k, v in LANGUAGES.items():
    print(f'{k}: {v}')

dest = input('ввод: ')

translator = Translator()
translations = translator.translate(data, dest=dest)
print(translations.text)

# print(f'{title} {text} {author} {date}')
# print(LANGUAGES)


# print(translator.translate('안녕하세요.'))
# print(translator.translate('안녕하세요.', dest='ja'))
# print(translator.translate('veritas lux mea', src='la'))

# translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.kr',
#     ])

# for translation in translations:
#     print(translation.origin, ' -> ', translation.text)
