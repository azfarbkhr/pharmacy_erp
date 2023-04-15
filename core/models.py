from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)

        if user and self._state.adding:
            self.created_by = user

        if user:
            self.updated_by = user

        super().save(*args, **kwargs)        

class organization(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    logo_url = models.CharField(max_length=2083, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Organizations'

    
class organization_user(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ' - ' + self.organization.name + ' - ' + ('Owner' if self.is_owner else 'User')

    class Meta:
        verbose_name_plural = 'Organization & User Relations'


class product(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    short_name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    bar_code = models.CharField(max_length=20, null=True, blank=True)
    sale_price = models.FloatField(default=0.0)
    unit_of_measure_type = models.ForeignKey('product_unit_of_measure', on_delete=models.CASCADE, null=True, blank=True)
    quantity_in_stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083, null=True, blank=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name_plural = 'Products'

class product_unit_of_measure(BaseModel):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Product Unit of Measure'

class product_price_history(BaseModel):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    price = models.FloatField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.product.name
    
    class Meta:
        verbose_name_plural = 'Price History'

class party(BaseModel):
    PARTY_TYPES = (
        ('Retail Customer', 'Retail Customer'),
        ('Hospital', 'Hospital'),
        ('Corporate Customer', 'Corporate'),
        ('Vendor', 'Vendor'),
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, choices=PARTY_TYPES, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name or 'None') + ' - ' + (self.type or 'None')

    class Meta:
        verbose_name_plural = 'Parties'
  
class invoice_header(BaseModel):
    INVOICE_TYPES = (
        ('Sale', 'Sale'),
        ('Return', 'Return'),
        ('Purchase', 'Purchase'),
    )

    party = models.ForeignKey(party, on_delete=models.CASCADE, null=True, blank=True)
    invoice_type = models.CharField(max_length=100, null=True, choices=INVOICE_TYPES, blank=True)
    invoice_number = models.CharField(max_length=100, null=True, blank=True)
    invoice_date = models.DateTimeField(null=True, blank=True)
    total_amount = models.FloatField(default=0.0)
    due_amount = models.FloatField(default=0.0)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.invoice_number + ' - ' + self.party.name or 'None'
    
    class Meta:
        verbose_name_plural = 'Invoices'
    
class invoice_detail(BaseModel):
    invoice = models.ForeignKey(invoice_header, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.invoice.invoice_number + ' - ' + self.product.name
    
    class Meta:
        verbose_name_plural = 'Invoice Details'

class invoice_payment(BaseModel):
    PAYMENT_TYPES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    )

    invoice = models.ForeignKey(invoice_header, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(null=True, blank=True)
    amount = models.FloatField(default=0.0)
    payment_type = models.CharField(max_length=100, null=True, choices=PAYMENT_TYPES, blank=True)
    card_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.invoice.invoice_number + ' - ' + str(self.amount)

    class Meta:
        verbose_name_plural = 'Payments'


