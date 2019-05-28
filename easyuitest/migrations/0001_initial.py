# Generated by Django 2.1.7 on 2019-05-15 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users_msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('role', models.CharField(max_length=32)),
                ('creator', models.CharField(max_length=32)),
                ('createTime', models.DateTimeField()),
                ('editor', models.CharField(max_length=32)),
                ('editTime', models.DateTimeField()),
                ('isValid', models.CharField(default='N', max_length=2)),
            ],
        ),
    ]
