# Generated by Django 4.2.2 on 2023-11-07 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0008_remove_bus_stu_student_bus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=500)),
                ('faculty_position', models.CharField(max_length=500)),
                ('faculty_salary', models.CharField(max_length=100)),
                ('school_of_faculty', models.CharField(max_length=500)),
                ('sch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crud.school')),
            ],
        ),
        migrations.RemoveField(
            model_name='salary',
            name='tech',
        ),
        migrations.DeleteModel(
            name='clark',
        ),
        migrations.DeleteModel(
            name='salary',
        ),
    ]
