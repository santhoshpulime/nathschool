# Generated by Django 4.0.2 on 2022-07-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_student_marks_t_p'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_marks',
            name='telugu',
            field=models.TextField(blank=True, default='abs'),
        ),
    ]