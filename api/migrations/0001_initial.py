# Generated by Django 4.0.4 on 2022-05-30 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('detailed_description', models.TextField()),
                ('short_description', models.CharField(max_length=300)),
            ],
        ),
    ]
