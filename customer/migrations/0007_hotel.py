# Generated by Django 3.1.5 on 2021-01-12 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_agenttable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
