# Generated by Django 4.2 on 2023-04-26 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0009_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]