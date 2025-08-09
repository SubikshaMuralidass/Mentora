# models.py

from django.db import models

class Question(models.Model):
    text = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()

    def __str__(self):
        return self.text

class TestResult(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option_text = models.TextField()
    sentiment = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.selected_option_text[:30]} - {self.sentiment}"
