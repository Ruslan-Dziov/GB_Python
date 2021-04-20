"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from translate import Translator
translator = Translator(from_lang='en', to_lang='russian')
f_ru = open('hw_4-ru.txt', 'w', encoding="utf-8")
with open('hw_4.txt', 'r') as f:
    for line in f:
        translation = translator.translate(line)
        print(translation)
        f_ru.write(translation + '\n')
f_ru.close()
