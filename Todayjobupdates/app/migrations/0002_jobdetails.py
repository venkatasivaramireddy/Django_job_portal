# Generated by Django 2.2.5 on 2019-11-07 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='jobimages')),
            ],
        ),
    ]
