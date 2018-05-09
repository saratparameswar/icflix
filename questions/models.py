# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class UserModel(models.Model):
    SEX_CHOICES = (
        ('', 'SEX'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('P', 'Prefer not to say'),
    )

    user = models.OneToOneField(User)

    first_name = models.CharField(
        max_length=255)
    last_name = models.CharField(
        max_length=255,
        blank=True)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES, blank=True)

    added_on = models.DateTimeField(
        auto_now_add=True)
    updated_on = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.first_name


class Questions(models.Model):
    asked_by = models.ForeignKey(UserModel)
    question = models.TextField()
    is_private = models.BooleanField(default=False)
    added_on = models.DateTimeField(
        auto_now_add=True)
    updated_on = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.question


class Answers(models.Model):
    question = models.ForeignKey(Questions, related_name="question_answers")
    answered_by = models.ForeignKey(UserModel, related_name="answered_questions")
    answer = models.TextField()
    added_on = models.DateTimeField(
        auto_now_add=True)
    updated_on = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.answer


class Tenant(UserModel):
    key = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=True)