# Generated by Django 3.0.2 on 2020-03-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_groupusertable_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupid', models.IntegerField()),
                ('notifId', models.IntegerField()),
            ],
        ),
    ]
