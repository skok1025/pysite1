# Generated by Django 2.2.2 on 2019-06-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contents', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('reg_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
