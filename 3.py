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
    data_start = CharField(column_name='data_start', max_length=8)
    data_end = CharField(column_name='data_end', max_length=8)

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
    students = [{'id': 1, 'name':'Max', 'surname':'Brooks', 'age': 24, 'city':'Spb'},
{'id': 2, 'name':'John', 'surname':'Stones', 'age': 15, 'city':'Spb'},
{'id': 3, 'name':'Andy', 'surname':'Wings', 'age': 45, 'city':'Manchester'},
{'id': 4, 'name':'Kate', 'surname':'Brooks', 'age': 34, 'city':'Spb'}]

    courses = [{'id':1, 'name':'python', 'data_start':'21.07.21', 'data_end':'21.08.21'},
{'id':2, 'name':'java', 'data_start':'13.07.21', 'data_end':'16.08.21'}]

    student_courses = [{ 'student_id': 1, 'course_id': 1},
{ 'student_id': 2, 'course_id': 1},
{ 'student_id': 3, 'course_id': 1},
{ 'student_id': 4, 'course_id': 2}]

    Students.create_table()
    Courses.create_table()
    Student_Courses.create_table()

    Students.insert_many(students).execute()
    Courses.insert_many(courses).execute()
    Student_Courses.insert_many(student_courses).execute()



def requests():
    query1 = Students.select().where(Students.age > 30)
    for q in query1:
        print('students over 30: ', q.name)


    query2 = Students.select().join(Student_Courses).where(Student_Courses.course_id == 1)

    for i in query2:
        print('students learning python: ', i.name)


    query3 = Students.select().join(Student_Courses).where(Student_Courses.course_id == 1, Students.city == 'Spb')

    for k in query3:
        print('students learning python and living in Spb: ', k.name)


if not os.path.exists('db1.sqlite'):
    db_creation()
requests()