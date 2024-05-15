import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('academy.db')
cursor = conn.cursor()

# Запрос 1: Вывести таблицу кафедр в обратном порядке
cursor.execute("SELECT department_name, department_id, faculty_id FROM Departments ORDER BY department_id DESC")
rows = cursor.fetchall()
print("Запрос 1:")
for row in rows:
    print(row)

# Запрос 2: Вывести названия групп и их рейтинги с уточнением имен полей именем таблицы
cursor.execute("SELECT group_name AS GroupName, group_rating AS Rating FROM Groups")
rows = cursor.fetchall()
print("\nЗапрос 2:")
for row in rows:
    print(row)

# Запрос 3: Вывести для преподавателей их фамилию, процент ставки по отношению к надбавке и процент ставки по отношению к зарплате
cursor.execute("SELECT last_name, bonus_rate*100 AS BonusRatePercent, (salary + bonus)/salary*100 AS TotalRatePercent FROM Employees WHERE job_title='Professor' AND salary > 1050")
rows = cursor.fetchall()
print("\nЗапрос 3:")
for row in rows:
    print(row)

# Запрос 4: Вывести таблицу факультетов в указанном формате
cursor.execute("SELECT 'The dean of faculty ' || faculty_name || ' is ' || dean_name FROM Faculties")
rows = cursor.fetchall()
print("\nЗапрос 4:")
for row in rows:
    print(row[0])

# Запрос 5: Вывести фамилии преподавателей, которые являются профессорами и ставка которых превышает 1050
cursor.execute("SELECT last_name FROM Employees WHERE job_title='Professor' AND salary > 1050")
rows = cursor.fetchall()
print("\nЗапрос 5:")
for row in rows:
    print(row[0])

# Запрос 6: Вывести названия кафедр с фондом финансирования меньше 11000 или больше 25000
cursor.execute("SELECT department_name FROM Departments WHERE funding < 11000 OR funding > 25000")
rows = cursor.fetchall()
print("\nЗапрос 6:")
for row in rows:
    print(row[0])

# Запрос 7: Вывести названия факультетов, кроме факультета "Computer Science"
cursor.execute("SELECT faculty_name FROM Faculties WHERE faculty_name != 'Computer Science'")
rows = cursor.fetchall()
print("\nЗапрос 7:")
for row in rows:
    print(row[0])

# Запрос 8: Вывести фамилии и должности преподавателей, которые не являются профессорами
cursor.execute("SELECT last_name, job_title FROM Employees WHERE job_title != 'Professor'")
rows = cursor.fetchall()
print("Запрос 8:")
for row in rows:
    print(row)

# Запрос 9: Вывести фамилии, должности, ставку и надбавку ассистентов, у которых надбавка в диапазоне от 160 до 550
cursor.execute("SELECT last_name, job_title, salary, bonus FROM Employees WHERE job_title='Assistant' AND bonus BETWEEN 160 AND 550")
rows = cursor.fetchall()
print("\nЗапрос 9:")
for row in rows:
    print(row)

# Запрос 10: Вывести фамилии и ставки ассистентов
cursor.execute("SELECT last_name, salary FROM Employees WHERE job_title='Assistant'")
rows = cursor.fetchall()
print("\nЗапрос 10:")
for row in rows:
    print(row)

# Запрос 11: Вывести фамилии и должности преподавателей, которые были приняты на работу до 01.01.2000
cursor.execute("SELECT last_name, job_title FROM Employees WHERE hire_date < '2000-01-01'")
rows = cursor.fetchall()
print("\nЗапрос 11:")
for row in rows:
    print(row)

# Запрос 12: Вывести названия кафедр, которые в алфавитном порядке располагаются до кафедры "Software Development"
cursor.execute("SELECT department_name AS 'Name of Department' FROM Departments WHERE department_name < 'Software Development' ORDER BY department_name")
rows = cursor.fetchall()
print("\nЗапрос 12:")
for row in rows:
    print(row)

# Запрос 13: Вывести фамилии ассистентов, имеющих зарплату не более 1200
cursor.execute("SELECT last_name FROM Employees WHERE job_title='Assistant' AND (salary + bonus) <= 1200")
rows = cursor.fetchall()
print("\nЗапрос 13:")
for row in rows:
    print(row)

# Запрос 14: Вывести названия групп 5-го курса, имеющих рейтинг в диапазоне от 2 до 4
cursor.execute("SELECT group_name FROM Groups WHERE course_number=5 AND group_rating BETWEEN 2 AND 4")
rows = cursor.fetchall()
print("\nЗапрос 14:")
for row in rows:
    print(row)

# Запрос 15: Вывести фамилии ассистентов со ставкой меньше 550 или надбавкой меньше 200
cursor.execute("SELECT last_name FROM Employees WHERE job_title='Assistant' AND (salary < 550 OR bonus < 200)")
rows = cursor.fetchall()
print("\nЗапрос 15:")
for row in rows:
    print(row)

# Закрытие соединения с базой данных
conn.close()
