from django.views.generic import View
from django.shortcuts import render
from questions.models import Questions, Answers
from request_log.models import LogApi

class Home(View):
    template_name = 'home.html'


    def get(self, request):
        context = {}
        ques = Questions.objects.all().count()
        ans = Answers.objects.all().count()
        apis = LogApi.objects.all().count()
        context['questions'] = ques
        context['ans'] = ans
        context['apis'] = apis
        return render(request, self.template_name, context)