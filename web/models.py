from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    url = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Loan_type(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    loan_interest = models.FloatField()
    loan_amount = models.IntegerField()
    loan_fee = models.FloatField()
    loan_term = models.IntegerField()
    
    def save(self):
        self.save()
    
    def __str__(self):
        return self.title
    