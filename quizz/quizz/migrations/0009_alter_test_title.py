# Generated by Django 3.2.9 on 2021-11-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0008_alter_test_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]