import string
import docx         # для работы с вордом
import pandas as pd  # для работы с Excel
import matplotlib.pyplot as plt # для таблицы визуальной

doc = docx.Document('lion.docx')

text = []
all_text = ''
stat = {}
symbols = {}

for paragraph in doc.paragraphs:
    text.append(paragraph.text)             # получаем массив строк, в которых находятся абзацы


for i in text:                              # создаем один единый текст в виде одной строки
    all_text += i

text = all_text.split()                     # делим на слова

for i in text:
    if i in stat:
        stat[i] += 1
    else:
        stat[i] = 1

# Проходим по каждому символу во всём тексте
for char in all_text:
    Lower = char.lower() # делаем все бувы под один регистор
    # Учитываем только буквы игноря пробелы и знаки
    if Lower.isalpha():
        if Lower in symbols:
            symbols[Lower] += 1
        else:
            symbols[Lower] = 1


total = sum(stat.values())

# Создаём таблицу
Tab = pd.DataFrame.from_dict(
    stat,
    orient='index',
    columns=['Частота, раз']
)


Tab['Частота (%)'] = (Tab['Частота, раз'] / total * 100).round(2)   # Добавляем процентный столбец


Tab.index.name = 'Слово'    # Задаём имя индекса

# Сохраняем в Excel
output_file = 'Результат.xlsx'
Tab.to_excel(output_file, index=True)

# создаем таблицу для букв
plt.figure(figsize=(12, 6))  # размер холста: ширина 12, высота 6 дюймов


# сортируем буквы по алфавиту
sorted_symbols = sorted(symbols.keys())  # буквы в алфавитном порядке
long = [symbols[letter] for letter in sorted_symbols]  # их частота


# Строим столбцы 
plt.bar(
    sorted_symbols,      
    long,        
    color='skyblue',    
    edgecolor='black'    
)

# Подписи и заголовок
plt.xlabel('Буква', fontsize=12)                    # по оси X
plt.ylabel('Частота встречаемости, раз', fontsize=12)     # по оси Y
plt.title('Частота встречаемости букв в тексте', fontsize=14, fontweight='bold')  # заголовок

plt.tight_layout() # чтобы подписи не обрезались



# Показываем график на экране
plt.show()