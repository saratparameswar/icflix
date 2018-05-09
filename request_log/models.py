from django.db import models
from questions.models import Tenant



class LogApi(models.Model):
    tenant = models.ForeignKey(Tenant)
    data = models.TextField()
    added_on = models.DateTimeField(
        auto_now_add=True)
    updated_on = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.tenant.first_name

