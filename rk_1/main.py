class Catalog:
    def __init__(self, catalog_id, name):
        self.catalog_id = catalog_id
        self.name = name

class File:
    def __init__(self, file_id, title, size, catalog_id=None):
        self.file_id = file_id
        self.title = title
        self.size = size
        self.catalog_id = catalog_id

class Link:
    def __init__(self, file_id, catalog_id):
        self.file_id = file_id
        self.catalog_id = catalog_id

# Тестовые данные
catalogs = [
    Catalog(1, "Рабочий каталог файлов"),
    Catalog(2, "Учёба"),
    Catalog(3, "Файлы отпуска 2024"),
    Catalog(4, "Каталог детских фото"),
    Catalog(5, "Каталог файлов со школы")
]

files = [
    File(1, "Анализ рынка труда.txt", 150, 1),
    File(2, "Сводная таблица 2024.xlsx", 320.50, 1),
    File(3, "ДЗ_социология.docx", 400, 2),
    File(4, "Маша фото 22.08.2024.png", 750, 4),
    File(5, "Алиса и Маша фото.png", 322, 4),
    File(6, "5А класс.png", 300, 5),
    File(7, "Альпы фото.png", 750, 3)
]

links = [
    Link(1, 1),
    Link(2, 1),
    Link(3, 2),
    Link(4, 3),
    Link(5, 3),
    Link(5, 4),
    Link(7, 3)
]

n1 = [i for i in catalogs if "каталог" in i.name.lower()]
d_1 = {i.name: [j.title for j in files if j.catalog_id == i.catalog_id] for i in n1}
print("Запрос 1. Каталоги с 'каталог' в названии и их файлы:")
for key in d_1:
    print(f'{key}: {", ".join(map(str, d_1[key]))}')

n2 = []
for i in catalogs:
    sizes = [j.size for j in files if j.catalog_id == i.catalog_id]
    if sizes:
        avg = round((sum(sizes) / len(sizes)), 2)
        n2.append((i.name, avg))
n2 = sorted(n2, key=lambda x: x[1])
print("\nЗапрос 2. Каталоги со средним размером файлов (от меньшего к большему):")
for name, avg in n2:
    print(f"{name}: {avg}")

file_a = [i for i in files if i.title[0] == "А"]
n_3 = []
for file in file_a:
    res = []
    for i in links:
        for j in catalogs:
            if i.file_id == file.file_id and j.catalog_id == i.catalog_id:
                res.append(j.name)
    n_3.append([file.title, res])

print("\nЗапрос 3. Файлы на 'А', и их каталоги:")
for i in n_3:
    print(f'Файл "{i[0]}" находится в каталогах: {", ".join(i[1])}')