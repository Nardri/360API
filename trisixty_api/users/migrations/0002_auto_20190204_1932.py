# Generated by Django 2.1.5 on 2019-02-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='-LXtztbLkAdYcA7YcBn5', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
