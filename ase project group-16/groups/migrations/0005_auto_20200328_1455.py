# Generated by Django 3.0.2 on 2020-03-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20200328_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouptable',
            name='image',
            field=models.ImageField(default='group_pics/default.jpg', upload_to='group_pics'),
        ),
    ]
