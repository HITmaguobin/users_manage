# Generated by Django 2.1.7 on 2019-05-20 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyuitest', '0002_auto_20190515_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='url_manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_source', models.CharField(max_length=32)),
                ('link', models.URLField()),
                ('timeconfig', models.CharField(max_length=32)),
                ('isValid', models.CharField(max_length=2)),
            ],
        ),
    ]