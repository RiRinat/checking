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
