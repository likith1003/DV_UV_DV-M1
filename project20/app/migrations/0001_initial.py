# Generated by Django 4.2.14 on 2024-09-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('princy', models.CharField(max_length=50)),
                ('loc', models.CharField(max_length=50)),
            ],
        ),
    ]
