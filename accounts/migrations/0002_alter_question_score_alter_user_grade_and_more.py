# Generated by Django 4.2.2 on 2023-06-12 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(default='D', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
