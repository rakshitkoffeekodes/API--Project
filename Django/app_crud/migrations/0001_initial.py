# Generated by Django 4.2.2 on 2023-11-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=500)),
                ('school_address', models.CharField(max_length=1000)),
                ('school_city', models.CharField(max_length=200)),
                ('school_state', models.CharField(max_length=200)),
                ('school_Country', models.CharField(max_length=200)),
            ],
        ),
    ]
