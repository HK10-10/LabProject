# Generated by Django 4.2.4 on 2023-08-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='lab_mobno',
            field=models.IntegerField(),
        ),
    ]
