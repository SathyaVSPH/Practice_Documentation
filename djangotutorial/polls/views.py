#from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

def index(request):
    #return HttpResponse('Hello World. You\'re at the polls index.')
    #recent_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    questions_list = Question.objects.all()
    #res = [q.question_text for q in recent_questions]
    #output = ', '.join(res)
    context = {'question_list': questions_list}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    '''try:
        question = Question.objects.get(pk=question_id)
    
    except Question.DoesNotExist:
        raise Http404('Question does not exist.')
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

    #return HttpResponse('You\'re looking at the question {}.'.format(question_id))'''

    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = f'You\'re looking at the results of the question {question_id}'
    return HttpResponse(response)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question': question,
                   'error_message': 'You did\'t select a choice.'}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:Result', args=(question.id,)))

    #return HttpResponse('Your voting on the question %s.' % question_id)