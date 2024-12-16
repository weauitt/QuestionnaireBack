# Generated by Django 4.2.17 on 2024-12-14 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('one', 'QuestionsOne'), ('two', 'QuestionsTwo'), ('three', 'QuestionsThree')], default='one', max_length=10),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
