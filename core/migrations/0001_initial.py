# Generated by Django 4.2 on 2023-04-15 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='invoice_header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_type', models.CharField(choices=[('Sale', 'Sale'), ('Return', 'Return'), ('Purchase', 'Purchase')], max_length=100, null=True)),
                ('invoice_number', models.CharField(max_length=100, null=True)),
                ('invoice_date', models.DateTimeField(null=True)),
                ('total_amount', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('contact_number', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('logo_url', models.CharField(max_length=2083, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('short_name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=10, null=True, unique=True)),
                ('bar_code', models.CharField(max_length=20, null=True)),
                ('sale_price', models.FloatField(default=0.0)),
                ('quantity_in_stock', models.IntegerField(default=0)),
                ('image_url', models.CharField(max_length=2083, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(choices=[('Retail Customer', 'Retail Customer'), ('Hospital', 'Hospital'), ('Corporate Customer', 'Corporate'), ('Vendor', 'Vendor')], max_length=100, null=True)),
                ('contact_number', models.CharField(max_length=100, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization')),
            ],
        ),
        migrations.CreateModel(
            name='organization_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_owner', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='invoice_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('payment_type', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], max_length=100, null=True)),
                ('card_number', models.CharField(max_length=100, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.invoice_header')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization')),
            ],
        ),
        migrations.AddField(
            model_name='invoice_header',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization'),
        ),
        migrations.AddField(
            model_name='invoice_header',
            name='party',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.party'),
        ),
        migrations.CreateModel(
            name='invoice_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('discount', models.FloatField(default=0.0)),
                ('amount', models.FloatField(default=0.0)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.invoice_header')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
    ]
