from rest_framework import serializers
from .models import Test, Question, Choice, UserAnswers, UserTest, Category


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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class ChoiceSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

    def create(self, validated_data):
        return Choice(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.is_right = validated_data.get('is_right', instance.is_right)
        return instance


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

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.order = validated_data.get('order', instance.order)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False, exclude=['test'])
    categories = CategorySerializer(many=True, required=False)

    def validate_questions(self, attrs):
        orders = [question['order'] for question in attrs]
        if len(set(orders)) != len(orders):
            raise serializers.ValidationError("The order of questions"
                                              " should not be repeated")
        return attrs

    class Meta:
        model = Test
        fields = '__all__'

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        categories_data = validated_data.pop('categories', [])
        test = Test.objects.create(**validated_data)

        # create questions
        for ind, question_data in enumerate(questions_data):
            questions_data[ind]['test'] = test
        self.fields['questions'].create(questions_data)

        # add categories
        for category_data in categories_data:
            category_qs = Category.objects.filter(title=category_data.get('title'))
            if category_qs.exists():
                category = category_qs.first()
            else:
                category = Category.objects.create(**category_data)
            test.categories.add(category)
        return test

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories')

        instance.title = validated_data.get('title', instance.title)
        instance.complexity = validated_data.get('complexity', instance.complexity)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        instance.categories.clear()
        for category_data in categories_data:
            category_qs = Category.objects.filter(title=category_data.get('title'))
            if category_qs.exists():
                category = category_qs.first()
            else:
                category = Category.objects.create(**category_data)
            instance.categories.add(category)

        return instance


class UserAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = '__all__'


class UserTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        fields = '__all__'
