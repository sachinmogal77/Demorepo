# Generated by Django 4.1.2 on 2022-10-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('marks', models.FloatField()),
                ('course', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('qualification', models.CharField(max_length=30)),
            ],
        ),
    ]
