# Generated by Django 2.0.4 on 2018-09-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0008_auto_20180125_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helparticle',
            name='version',
            field=models.CharField(default='0.5.1', max_length=5),
        ),
    ]
