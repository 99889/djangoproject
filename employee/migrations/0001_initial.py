# Generated by Django 3.2.7 on 2021-10-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=800)),
                ('email', models.TextField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]