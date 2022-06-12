# Generated by Django 4.0 on 2021-12-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Crs_Code', models.IntegerField()),
                ('Crs_Name', models.CharField(max_length=100)),
                ('Sub_Code', models.IntegerField()),
                ('Crs_Initials', models.CharField(max_length=2)),
                ('Crs_Credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stf_id', models.IntegerField()),
                ('Stf_Fname', models.CharField(max_length=100)),
                ('Stf_Lname', models.CharField(max_length=100)),
                ('Stf_email', models.CharField(max_length=100)),
                ('Stf_Pass', models.CharField(max_length=100)),
                ('Stf_dob', models.DateTimeField()),
                ('Stf_Exp', models.IntegerField()),
                ('Sub_Code', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stu_id', models.IntegerField()),
                ('Stu_Fname', models.CharField(max_length=100)),
                ('Stu_Lname', models.CharField(max_length=100)),
                ('Stu_email', models.CharField(max_length=100)),
                ('Stu_Pass', models.CharField(max_length=100)),
                ('Stu_dob', models.DateTimeField()),
                ('Stu_grade', models.CharField(max_length=3)),
                ('Stu_marks', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_Code', models.IntegerField()),
                ('Sub_Name', models.CharField(max_length=100)),
                ('Crs_Code', models.IntegerField()),
                ('Sub_Grade', models.CharField(max_length=2)),
            ],
        ),
    ]