# Generated by Django 2.1.7 on 2019-05-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyuitest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_msg',
            name='createTime',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='users_msg',
            name='editTime',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='users_msg',
            name='isValid',
            field=models.CharField(max_length=2),
        ),
    ]
