from rest_framework import serializers
from .models import Test, Question, Choice, UserAnswers, UserTest


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if exclude is not None:
            # Drop any fields that are specified in the `exclude` argument.
            for field_name in exclude:
                self.fields.pop(field_name, None)


class ChoiceSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(DynamicFieldsModelSerializer):
    choices = ChoiceSerializer(many=True, required=False, exclude=['question'])

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        choices_data = validated_data.pop('choices', [])
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False, exclude=['test'])

    def validate_questions(self, attrs):
        orders = [question['order'] for question in attrs]
        if len(set(orders)) != len(orders):
            raise serializers.ValidationError("Orders of questions"
                                              " should not be repeated")
        return attrs

    class Meta:
        model = Test
        fields = '__all__'

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        test = Test.objects.create(**validated_data)
        for ind, question_data in enumerate(questions_data):
            questions_data[ind]['test'] = test
        self.fields['questions'].create(questions_data)
        return test

