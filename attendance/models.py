from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    subteams = (
            ('m', 'Mechanical'),
            ('e', 'Electrical'),
            ('p', 'Programming'),
            ('d', 'Media'),
    )
    birthmonths = (
            (0, 'NEW'),
            (1, 'Jan'),
            (2, 'Feb'),
            (3, 'Mar'),
            (4, 'Apr'),
            (5, 'May'),
            (6, 'Jun'),
            (7, 'Jul'),
            (8, 'Aug'),
            (9, 'Sept'),
            (10, 'Oct'),
            (11, 'Nov'),
            (12, 'Dec'),
    )
    birthmonth = models.PositiveSmallIntegerField('student birthmonth', choices=birthmonths, default=0)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    subteam = models.CharField(max_length=1, choices=subteams, blank=True)

    def meetings_attended(self):
        return len(SignIn.objects.filter(student_id=self))

    def percent_attended(self):
        num_meetings = len(SignIn.objects.all())

        if num_meetings:
            return str(round(self.meetings_attended()/num_meetings*100,2)) + "%"
        else:
            return 0

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Meeting(models.Model):
    meeting_category = (
            ('u', 'MOE U'),
            ('b', 'Build'),
            ('n', 'Non-mandatory'),
            ('o', 'Other'),
    )

    date = models.DateField('meeting date',primary_key=True)
    time = models.TimeField('meeting time')
    category = models.CharField(max_length=1, choices=meeting_category)

    students = models.ManyToManyField(Student, through="SignIn")

    def __str__(self):
        return datetime.datetime.strftime(self.date, '%x')

class SignIn(models.Model):
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    time = models.TimeField()

    class Meta:
        unique_together = ('meeting_id','student_id')
