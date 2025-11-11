import matplotlib.pyplot as plt
import pandas as pd             # импорты

# parquet в csv
df = pd.read_parquet('titanic.parquet')
df.to_csv('titanic.csv')

df = pd.read_csv('titanic.csv') # Чтение данных


survived = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)    # таблица


surv_percent = survived.div(survived.sum(axis=1), axis=0) * 100 # проценты в оси y

#график
surv_percent.plot(kind='bar', stacked=True, color=['blue', 'orange'])
plt.title('Процент выживших пассажиров Титаника по классам билетов')
plt.xlabel('Класс билета')
plt.ylabel('Процент пассажиров')
plt.xticks(rotation=0)  # Поворот для нормального отображения оси X
plt.legend(['Не выжил', 'Выжил'])  # Легенда

plt.show()