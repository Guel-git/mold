from django.db.models.query import RawQuerySet
from django.shortcuts import redirect, render
from .models import *
from community.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def grade(request):
    return render(request, 'grade.html')


def creategrade(request):
    grade = Grade()
    grade.author = request.user
    grade.title = request.POST.get('title')
    grade.sending = request.POST.get('sending')
    grade.name = request.POST.get('name')
    grade.subject = request.POST.get('subject')
    grade.test = request.POST.get('test')
    grade.save()
    return redirect('article')


def meeting(request):
    return render(request, 'meeting.html')


def createmeeting(request):
    meeting = Meeting()
    meeting.author = request.user
    meeting.title = request.POST.get('title')
    meeting.sending = request.POST.get('sending')
    meeting.name = request.POST.get('name')
    meeting.background = request.POST.get('background')
    meeting.time = request.POST.get('time')
    meeting.save()
    return redirect('article')


def attendance(request):
    return render(request, 'attendance.html')


def createattendance(request):
    attendance = Attendance()
    attendance.author = request.user
    attendance.title = request.POST.get('title')
    attendance.sending = request.POST.get('sending')
    attendance.name = request.POST.get('name')
    attendance.subject = request.POST.get('subject')
    attendance.evidence = request.POST.get('evidence')
    attendance.date = request.POST.get('date')
    attendance.save()
    return redirect('article')


def recommendation(request):
    return render(request, 'recommendation.html')


def createrecommendation(request):
    recommendation = Recommendation()
    recommendation.author = request.user
    recommendation.title = request.POST.get('title')
    recommendation.sending = request.POST.get('sending')
    recommendation.name = request.POST.get('name')
    recommendation.event = request.POST.get('event')
    recommendation.intro = request.POST.get('intro')
    recommendation.detail = request.POST.get('detail')
    recommendation.save()
    return redirect('article')


def template(request):
    template = Template.objects
    return render(request, 'template.html', {'templates': template})


@login_required
def mypage1(request):
    logged_in_user = request.user
    logged_in_user_grades = Grade.objects.filter(author=request.user)
    logged_in_user_meetings = Meeting.objects.filter(author=request.user)
    logged_in_user_attendance = Attendance.objects.filter(author=request.user)
    logged_in_user_recommendation = Recommendation.objects.filter(
        author=request.user)

    return render(request, 'article.html', {'grades': logged_in_user_grades, 'meetings': logged_in_user_meetings, 'recommendations': logged_in_user_recommendation, 'attendances': logged_in_user_attendance})


@login_required
def mypage(request):
    logged_in_user = request.user
    reply = Reply.objects.filter(created_by=request.user)
    community = Community.objects.all()
    # community = Community.objects.filter(author=Reply.objects.filter(created_by=request.use)
    return render(request, 'mypage.html', {'replys': reply, 'communitys': community})
