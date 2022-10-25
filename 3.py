from peewee import *
import os.path
conn = SqliteDatabase('db1.sqlite')

class Students(Model):
    id = PrimaryKeyField(column_name='id', primary_key=True)
    name = CharField(column_name='name', max_length=32)
    surname = CharField(column_name='surname', max_length=32)
    age = IntegerField(column_name='age')
    city = CharField(column_name='city', max_length=12)

    class Meta:
        db_table = 'students'
        database = conn

class Courses(Model):
    id = PrimaryKeyField(column_name='id', primary_key=True)
    name = CharField(column_name='name', max_length=32)
    time_start = CharField(column_name='time_start', max_length=8)
    time_end = CharField(column_name='time_end', max_length=8)

    class Meta:
        db_table = 'courses'
        database = conn


class Student_Courses(Model):
    student_id = ForeignKeyField(Students, to_field='id')
    course_id = ForeignKeyField(Courses, to_field='id')

    class Meta:
        db_table = 'student_courses'
        database = conn


def db_creation():
    students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
                (3, 'Andy', 'Wings', 45, 'Manchester'), (4, 'Kate', 'Brooks', 34, 'Spb')]

    courses = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]
    student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

    Students.create_table()
    Courses.create_table()
    Student_Courses.create_table()

    Students.insert_many(students).execute()
    Courses.insert_many(courses).execute()
    Student_Courses.insert_many(student_courses).execute()

if not os.path.exists('db1.sqlite'):
    db_creation()


query1 = Students.select().where(Students.age > 30)
for q in query1:
    print('students over 30: ', q.name)


query2 = Students.select().join(Student_Courses).where(Student_Courses.course_id == 1)

for i in query2:
    print('students learning python: ', i.name)


query3 = Students.select().join(Student_Courses).where(Student_Courses.course_id == 1, Students.city == 'Spb')

for k in query3:
    print('students learning python and living in Spb: ', k.name)


#При вызове запросов ответы дублируются. Не могу разобраться