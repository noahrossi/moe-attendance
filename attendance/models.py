from django.db import models
import time

# Create your models here.
class Student(models.Model):
    birthday = models.DateTimeField('student birthday')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Meeting(models.Model):
    meeting_category = (
            ('u', 'MOE U'),
            ('b', 'Build'),
            ('e', 'Non-mandatory'),
            ('o', 'Other'),
    )

    date = models.DateTimeField('meeting date',primary_key=True)
    category = models.CharField(max_length=1, choices=meeting_category)

    students = models.ManyToManyField(Student, through="SignIn")

    def __str__(self):
        return time.strftime(date, '%x') + ' ' + meeting_category[category]

class SignIn(models.Model):
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    time = models.TimeField()

    class Meta:
        unique_together = ('meeting_id','student_id')
