# Generated by Django 4.2 on 2023-04-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_invoice_payment_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_header',
            name='due_amount',
            field=models.FloatField(default=0.0),
        ),
    ]
