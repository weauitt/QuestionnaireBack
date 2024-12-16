from rest_framework import serializers
from .models import Question, Option

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'is_required', 'options']

class QuestionSetSerializer(serializers.Serializer):
    QuestionsOne = QuestionSerializer(many=True)
    QuestionsTwo = QuestionSerializer(many=True)
    QuestionsThree = QuestionSerializer(many=True)
    # Добавьте сюда все остальные наборы вопросов (QuestionsFour, QuestionsFive и т.д.)