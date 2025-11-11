import docx
import string



doc = docx.Document('lion.docx')


text = []
all_text = ''
stat = {}

for paragraph in doc.paragraphs:
    text.append(paragraph.text)             # получаем массив строк, в которых находятся обзацы


for i in text:                              # создаем один единый текст в виде одной строки
    all_text += i

text = all_text.split()                     # делим на слова

for i in text:
    if i in stat:
        stat[i] += 1
    else:
        stat[i] = 1


print(stat)
