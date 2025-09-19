#from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    #return HttpResponse('Hello World. You\'re at the polls index.')
    recent_questions = Question.objects.order_by('-pub_date')[:5]
    res = [q.question_text for q in recent_questions]
    output = ', '.join(res)
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse('You\'re looking at the question {}.'.format(question_id))

def results(request, question_id):
    response = f'You\'re looking at the results of the question {question_id}'
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse('Your voting on the question %s.' % question_id)