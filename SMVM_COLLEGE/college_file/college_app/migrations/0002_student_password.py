# Generated by Django 5.1.3 on 2024-12-04 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=models.CharField(max_length=100, primary_key=True, serialize=False), max_length=50),
        ),
    ]
