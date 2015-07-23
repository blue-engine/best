from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

"""
A grouping of courses that is managed by a principal,
usually represented by one building or geographical location
"""
class School(models.Model):
    code = models.CharField(max_length=128)
    name = models.CharField(max_length=256)

    def __str__(self):
        return "{} - {}".format(self.code, self.name)


"""
a way in which courses are categorized (math, literacy, etc)
"""
class ContentArea(models.Model):
    code = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return "{} - {}".format(self.code, self.description)


"""
a specific topic of a particular content area that spans a time period (quarter, semester)
"""
class Course(models.Model):
    code = models.CharField(max_length=128)
    content_area = models.ForeignKey(ContentArea)
    description = models.CharField(max_length=256)
    
    def __str__(self):
        return "{} - {}".format(self.code, self.description)

"""
an individual that is tasked with teaching course content to students and
tracking the academic progress of students
"""
class Instructor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    school = models.ForeignKey(School)
    user = models.ForeignKey(AUTH_USER_MODEL, null=True)


    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


"""
the members of groups for which metrics are tracked
"""
class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    osis_number = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    school = models.ForeignKey(School)

    def __str__(self):
        return "{} - {} {}".format(
            self.osis_number,
            self.first_name,
            self.last_name
        )

"""
a subset of a course that meets at a particular time in a specific school
"""
class Section(models.Model):
    code = models.CharField(max_length=128)
    course = models.ForeignKey(Course)
    school = models.ForeignKey(School)
    description = models.CharField(max_length=256)
    year_code = models.CharField(max_length=32)
    semester_code = models.CharField(max_length=32)

    def __str__(self):
        return "{} - {}".format(self.code, self.description)


"""
State-defined list of competencies that must be mastered to complete a course
"""
class Standard(models.Model):
    course = models.ForeignKey(Course)
    description = models.CharField(max_length=256)


"""
a particular lesson or objective that must be completed by
students for them to progress academically
"""
class LearningTarget(models.Model):
    code = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    
    def __str__(self):
        return "{} - {}".format(self.code, self.description)

"""
collection of students taught by an instructor
"""
class Group(models.Model):
    code = models.CharField(max_length=128)
    section = models.ForeignKey(Section)
    instructor = models.ForeignKey(Instructor)
    
    def __str__(self):
        return "{} - {}".format(self.code, self.section)

class GroupStudent(models.Model):
    group = models.ForeignKey(Group)
    student = models.ForeignKey(Student)
    date_entered = models.DateField('Date Entered')
    date_left = models.DateField('Date Left', null=True)


class Plan(models.Model):
    course = models.ForeignKey(Course)
    instructor = models.ForeignKey(Instructor)
    description = models.CharField(max_length=256)
    learning_target = models.ForeignKey(LearningTarget)
    dosage = models.IntegerField()
    exit_ticket_denominator = models.IntegerField()
    homework_denominator = models.IntegerField()
    quiz = models.BooleanField()

    def __str__(self):
        return self.description

class Report(models.Model):
    group = models.ForeignKey(Group)
    date = models.DateField()
    week = models.IntegerField()
    plan = models.ForeignKey(Plan, null=True)
    exported = models.BooleanField()

class ReportStudent(models.Model):
    ATTENDANCE_CHOICES = (
        (0, 'Present'),
        (1, 'Absent'),
        (2, 'Tardy')
    )
    HOMEWORK_CHOICES = (
        (0, 'Excused/No HW'),
        (1, 'Yes'),
        (2, 'No')
    )
    report = models.ForeignKey(Report)
    student = models.ForeignKey(Student)
    attendance = models.IntegerField(choices=ATTENDANCE_CHOICES)
    exit_ticket = models.IntegerField(null=True)
    homework_effort = models.IntegerField(choices=HOMEWORK_CHOICES)
    homework_accuracy = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return "{}, {}".format(
            self.student.first_name,
            self.student.last_name
        )
