import sqlite3

db = sqlite3.connect('module_8.db')

c = db.cursor()

#Создание таблицы student
c.execute("""CREATE TABLE IF NOT EXISTS student (
     id integer PRIMARY KEY,
     name varchar(32),
     surname varchar(32),
     age integer,
     city varchar(32)
 )""")


#Создание таблицы course
c.execute("""CREATE TABLE IF NOT EXISTS course (
     id integer PRIMARY KEY,
     name varchar(32),
     time_start text,
     time_end date text
 )""")


# Создание таблицы student_course
c.execute("""CREATE TABLE IF NOT EXISTS student_course (
     course_id integer,
     student_id integer
 )""")


c.execute("INSERT INTO course VALUES (1, 'python', '21.07.21', '21.08.21')")
c.execute("INSERT INTO course VALUES (2, 'java', '13.07.21', '16.08.21')")

c.execute("INSERT INTO student VALUES (1, 'Max', 'Brooks', 24, 'Spb')")
c.execute("INSERT INTO student VALUES (2, 'John', 'Stones', 15, 'Spb')")
c.execute("INSERT INTO student VALUES (3, 'Andy', 'Wings', 45, 'Manhester')")
c.execute("INSERT INTO student VALUES (4, 'Kate', 'Brooks', 34, 'Spb')")

c.execute("INSERT INTO student_course VALUES (1, 1)")
c.execute("INSERT INTO student_course VALUES (2, 1)")
c.execute("INSERT INTO student_course VALUES (3, 1)")
c.execute("INSERT INTO student_course VALUES (4, 2)")

c.execute("DROP TABLE student_course")
c.execute("DROP TABLE student")
c.execute("DROP TABLE course")

#Имена студентов старше 30
c.execute("SELECT name FROM student WHERE age > 30")
print(c.fetchall())

# Имена студентов, проходящих курс по Python
c.execute("SELECT student.name FROM student_course JOIN student ON student_course.student_id = student.id WHERE course_id = 1;")
print(c.fetchall())

# Имена студентов, проходящих курс по Python и из Spb

c.execute("SELECT student.name FROM student_course JOIN student ON student_course.student_id = student.id WHERE course_id = 1 AND city = 'Spb';")
print(c.fetchall())


db.commit()
db.close()

# Два последних запроса работают только для одного человека. Что не так?
# Третье задание скину позднее 