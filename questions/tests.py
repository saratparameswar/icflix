# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from questions.models import Tenant
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from questions.api_views import GetQuestionsAPI


# Create your tests here.
class GetQuestionsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@test.com', first_name='test', last_name='admin',
                                                         password='password')
        self.tenant = Tenant.objects.create(user=self.user,first_name="test_user", last_name="test",sex="M")
        self.key = self.tenant.key


    def test_GetQuestions(self):
        data = {'key':self.key, 'allow':True}
        factory = APIRequestFactory()
        request = factory.get('/questions/list/', data=data, format='json')
        view = GetQuestionsAPI.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)



