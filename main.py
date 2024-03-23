import sqlite3

db = sqlite3.connect('db.db')
cursor = db.cursor()

group = cursor.execute('''SELECT * FROM "pyspark.sql.DataFrame" ''').fetchall()
nogroup = []
for elem in group:
    if elem[0] is None:
        pass
    elif elem[1] == '':
        nogroup.append(elem[0])
    else:
        print(f"Имя продукта - {elem[0]}, Имя категории - {elem[1]}")
if not nogroup:
    pass
else:
    print(f'Без категории товары: {" ".join(nogroup)}')