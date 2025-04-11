import pandas as pd
import matplotlib.pyplot as plt

# Крок 1: Завантаження даних з урахуванням можливих нестандартних роздільників
df = pd.read_csv('data.csv', encoding='latin1', engine='python')

# Крок 2: Перейменовуємо перший стовпець на "Date"
df.rename(columns={df.columns[0]: 'Date'}, inplace=True)

# Крок 3: Виділяємо тільки дату з "дата,час", наприклад: "01/01/2011,00:00"
df['Date'] = pd.to_datetime(df['Date'].str.split(',').str[0], dayfirst=True)

# Крок 4: Робимо колонку 'Date' індексом
df.set_index('Date', inplace=True)

# Діагностика: показати перші рядки та список колонок
print("Перші рядки датафрейму:")
print(df.head(3))
print("\nСтовпці:", df.columns)

# Крок 5: Побудова графіку
plt.figure(figsize=(15, 10))
df.plot(ax=plt.gca(), title='Використання велодоріжок у 2011 році')
plt.xlabel('Дата')
plt.ylabel('Кількість велосипедистів')
plt.grid(True)
plt.tight_layout()
plt.show()

# Крок 6: Обчислення сумарного використання та найпопулярнішого місяця
df['Total'] = df.sum(axis=1)
monthly_totals = df.resample('M').sum()
most_popular_month = monthly_totals['Total'].idxmax().strftime('%B')

print(f"\n📅 Найпопулярніший місяць серед велосипедистів у 2011 році: {most_popular_month}")
