# Generated by Django 3.0.3 on 2020-07-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_auto_20200726_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='resource_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
