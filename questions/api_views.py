# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from questions.models import Questions, Answers
from serializer import AnswerSerializer, QuestionSerializer
from rest_framework import status
from questions import authentication
from request_log.mixins import RequestLogViewMixin
from rest_framework.permissions import IsAuthenticated

# Create your views here.





class GetQuestionsAPI(RequestLogViewMixin,APIView):
    serializer_class = QuestionSerializer
    """Get Params allow=False returns answers except answered by the logged in user, 
    else it returns all answers"""

    authentication_classes = (authentication.TenantAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allow = request.GET['allow']

        questions = Questions.objects.filter(is_private=False)
        serializer = self.serializer_class(questions, many=True, context={"user": 1,'allow':allow})
        return Response(serializer.data, status=status.HTTP_200_OK)



