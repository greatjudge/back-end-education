# Generated by Django 3.2.9 on 2021-11-21 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20211121_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quiz.question', verbose_name='вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.test', verbose_name='тест'),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('test', 'order')},
        ),
    ]
