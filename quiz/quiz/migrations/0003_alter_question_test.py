# Generated by Django 3.2.9 on 2021-11-21 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_test_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.test', verbose_name='тест'),
        ),
    ]
