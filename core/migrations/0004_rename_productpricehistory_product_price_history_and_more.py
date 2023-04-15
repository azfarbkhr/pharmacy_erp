# Generated by Django 4.2 on 2023-04-15 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_invoice_header_invoice_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductPriceHistory',
            new_name='product_price_history',
        ),
        migrations.AddField(
            model_name='product',
            name='unit_of_measure_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='product_unit_of_measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_of_measure_type', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity_in_stock', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
            options={
                'verbose_name_plural': 'Product Unit of Measure',
            },
        ),
    ]
