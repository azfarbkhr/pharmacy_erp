from django.contrib import admin
from .models import *

class BaseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(organization, BaseAdmin, 
    list_display = ('name', 'address', 'contact_number', 'email', 'logo_url', 'is_active', 'created_by', 'updated_by', 'created_at', 'updated_at'),

)

admin.site.register(organization_user, BaseAdmin,
    list_display = ('user', 'organization', 'is_owner', 'created_by', 'updated_by', 'created_at', 'updated_at'),
    list_filter = ('organization',),
)


admin.site.register(product, BaseAdmin,
    list_display = ('name', 'short_name', 'code', 'bar_code', 'sale_price', 'unit_of_measure_type', 'quantity_in_stock', 'image_url', 'organization', 'created_by', 'updated_by', 'created_at', 'updated_at'),
    list_filter = ('organization',),

)

admin.site.register(product_unit_of_measure, BaseAdmin,
    list_display = ('name', 'organization', 'created_by', 'updated_by', 'created_at', 'updated_at'),
    list_filter = ('organization',),
)
admin.site.register(product_price_history, BaseAdmin,                   
    list_display = ('product', 'price', 'created_by', 'updated_by', 'created_at', 'updated_at'),
)
admin.site.register(party, BaseAdmin, 
    list_display = ('name', 'contact_number', 'type', 'organization', 'created_by', 'updated_by', 'created_at', 'updated_at'),
    list_filter = ('organization',),

)

class invoice_detailsInline(admin.TabularInline):
    model = invoice_detail
    extra = 1

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)    

class invoice_paymentInline(admin.TabularInline):
    model = invoice_payment
    extra = 1

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
            


class invoice_headerAdmin(BaseAdmin):
    inlines = [invoice_detailsInline, invoice_paymentInline]

# register invoice_header model admin class
admin.site.register(invoice_header, invoice_headerAdmin, 
    list_display = ('invoice_number', 'invoice_date', 'party', 'organization', 'created_by', 'updated_by', 'created_at', 'updated_at'),
    list_filter = ('organization',),
)
