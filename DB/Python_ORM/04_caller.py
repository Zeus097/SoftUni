import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student


def add_students():
    student_1 = Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com'
    )
    student_1.save()

    student_2 = Student.objects.create(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com'
    )
    student_2.save()

    student_3 = Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com'
    )
    student_3.save()

    student_4 = Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com'
    )
    student_4.save()


def get_students_info():
    students = Student.objects.all()
    students_ls = []
    for student in students:
        students_ls.append(
            f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}"
        )

    return '\n'.join(students_ls)


def update_students_emails():
    students = Student.objects.all()
    for student in students:
        student.email = student.email.replace(student.email.split('@')[1], 'uni-students.com')

        student.save()


def truncate_students():
    students = Student.objects.all()
    for student in students:
        student.delete()


# # Test code
# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")
