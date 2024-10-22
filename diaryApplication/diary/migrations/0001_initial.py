# Generated by Django 5.1 on 2024-10-22 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('entry', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
