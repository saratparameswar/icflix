# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from questions.models import UserModel,Questions,Answers, Tenant

# Register your models here.
admin.site.register(UserModel)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Tenant)
