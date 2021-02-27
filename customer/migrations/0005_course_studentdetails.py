# Generated by Django 3.1.3 on 2020-12-23 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_account_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('mobileNo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=30)),
                ('students', models.ManyToManyField(to='customer.Student')),
            ],
        ),
    ]
