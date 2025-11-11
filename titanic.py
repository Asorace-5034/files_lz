import pandas as pd
import matplotlib.pyplot as plt


Tab = pd.read_parquet('titanic.parquet') # Читаем файл


Tab.to_csv('titanic.csv') # Переводим в csv и сохраняем


survival = Tab.groupby('Pclass')['Survived'].value_counts().unstack(fill_value=0)   # ГСчитаем выживших и погибших


survival_stats_norm = survival.div(survival.sum(axis=1), axis=0) * 100  #Переводим в проценты

# Данные для графика
classes = ['Первый класс', 'Второй класс', 'Третий класс']
survived = survival_stats_norm[1].values
not_survived = survival_stats_norm[0].values

# Создаём график
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_yticks([0, 50, 100])  
ax.set_yticklabels(['0%', '50%', '100%']) 
bars_1 = ax.bar(classes, survived, color='blue', label='Выжил')
bars_2 = ax.bar(classes, not_survived, bottom=survived, color='orange', label='Не выжил')

# Настройки графика
ax.set_ylim(0, 100)
ax.set_title('Выживаемость пассажиров Титаника', fontsize=16, pad=20)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Делаем легенду
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2)

plt.tight_layout()
plt.show()
