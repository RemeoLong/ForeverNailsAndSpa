# Generated by Django 2.2.16 on 2020-10-06 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_customer_visit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='clock_out',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.IntegerField(default=0, editable=False, max_length=9),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(default=0, editable=False, max_length=9),
        ),
    ]
