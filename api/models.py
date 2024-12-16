from django.db import models

class Question(models.Model):
    text = models.TextField()  # Текст вопроса
    is_required = models.BooleanField(default=True)  # Обязательный вопрос или нет

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)  # Варианты связаны с вопросом
    text = models.CharField(max_length=255)  # Текст варианта

    def __str__(self):
        return self.text
