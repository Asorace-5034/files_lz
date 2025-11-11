import matplotlib.pyplot as plt
import pandas as pd

# parquet в csv
par = pd.read_parquet('titanic.parquet')
par.to_csv('titanic.csv', index=False)

par = pd.read_csv('titanic.csv') # Чтение данных


surv = par.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)#новая таблица


surv_percent = surv.div(surv.sum(axis=1), axis=0) * 100 # проценты в оси y

#график
surv_percent.plot(kind='bar', stacked=True, color=['blue', 'orange'])
plt.title('Процент выживших пассажиров Титаника по классам билетов')
plt.xlabel('Класс билета')
plt.ylabel('Процент пассажиров')
plt.xticks(rotation=0)  # Поворот меток оси X
plt.legend(['Не выжил', 'Выжил'])  # Легенда

plt.show()