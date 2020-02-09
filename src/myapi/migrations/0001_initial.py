# Generated by Django 3.0.2 on 2020-02-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('vehicle', models.CharField(max_length=60)),
                ('human', models.BooleanField()),
            ],
        ),
    ]
