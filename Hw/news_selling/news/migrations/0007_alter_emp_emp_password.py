# Generated by Django 5.0 on 2023-12-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_emp_emp_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='Emp_password',
            field=models.IntegerField(),
        ),
    ]
