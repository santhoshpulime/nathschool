# Generated by Django 4.0.2 on 2022-07-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='opt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.TextField()),
                ('stu_name', models.TextField()),
                ('num_otp', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.TextField()),
                ('stu_class', models.TextField()),
                ('phone_number', models.TextField()),
                ('roll_num', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='student_marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.TextField()),
                ('stu_name', models.TextField()),
                ('stubject', models.TextField()),
                ('test_num', models.TextField(blank=True)),
                ('marks', models.TextField(blank=True, default='0')),
            ],
        ),
    ]