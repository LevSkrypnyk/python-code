import pandas as pd

df = pd.DataFrame({
    "Vitaly_Prikhodko": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10],
    "Dmytro_Kropyvnytskyi": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4],
    "Mikhail_Romanenko": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4],
    "Maxim_Deriemzlya": [12, 10, 7, 5, 8, 3, 8, 4, 5, 7],
    "Victoria_Zhuk": [10, 10, 10, 9, 8, 5, 7, 7, 7, 12],
    "Andrey_Kuryanov": [5, 7, 5, 4, 5, 7, 5, 4, 7, 8],
    "Oksana_Dubovets": [7, 8, 9, 8, 3, 9, 7, 5, 7, 10],
    "Nikita_Stroganov": [6, 7, 8, 9, 10, 10, 10, 10, 10, 9],
    "Karina_Nikolaenko": [2, 3, 5, 4, 5, 4, 4, 3, 5, 8]
})

# Виведення датафрейму
print(df)

# Агрегація по одному студенту
print("\nСереднє значення:", df["Vitaly_Prikhodko"].mean())
print("Сума:", df["Vitaly_Prikhodko"].sum())
print("Мінімум:", df["Vitaly_Prikhodko"].min())
print("Максимум:", df["Vitaly_Prikhodko"].max())

# Групування — середній бал кожного студента
print("\nСередній бал кожного студента:")
print(df.mean())
