from rest_framework import serializers
from .models import Test, Question, Choice, UserAnswers, UserTest


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        extra_kwargs = {'test': {'required': False}}


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = '__all__'
        extra_kwargs = {'test': {'required': False}}

    def create(self, validated_data):
        choices_data = validated_data.pop('choices', [])
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        questions_data = validated_data.pop('choices', [])
        test = Test.objects.create(**validated_data)
        for question_data in questions_data:
            Choice.objects.create(question=test, **question_data)
        return test

