# Generated by Django 4.2 on 2023-04-25 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0005_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='excel_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
