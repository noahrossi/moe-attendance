from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Meeting, Student, SignIn
import datetime
from django.shortcuts import get_list_or_404, get_object_or_404


def index(request):
    today = datetime.datetime.strftime(datetime.datetime.now(), '%A, %B %d')
    time = datetime.datetime.strftime(datetime.datetime.now(), '%I:%M %p')

    try:
        current_meeting = Meeting.objects.get(pk=datetime.datetime.now().date())
    except Meeting.DoesNotExist:
        current_meeting = None

    context = {'today': today, 'time': time, 'meeting': current_meeting}

    return render(request, 'index.html', context)

def month(request, month_num):
    students = get_list_or_404(Student.objects.order_by('last_name'), birthmonth=month_num)
    context = {'students': students}

    return render(request, 'month.html', context)

def signin(request, userid):
    student_id = get_object_or_404(Student, pk=userid)
    meeting_id = get_object_or_404(Meeting, pk=datetime.datetime.now().date())

    SignIn.objects.create(student_id=student_id, meeting_id=meeting_id,
            time = datetime.datetime.now().time())

    if student_id.birthmonth == 0:
        return HttpResponseRedirect('new/' + str(student_id.id))

    return HttpResponseRedirect('/attendance')

def new(request, userid):
    context = {'user_id': userid}

    return render(request, 'new.html', context)

def change_month(request, userid, month_num):
    student_id = get_object_or_404(Student, pk=userid)

    student_id.birthmonth = month_num

    student_id.save()

    return HttpResponseRedirect('/attendance')
