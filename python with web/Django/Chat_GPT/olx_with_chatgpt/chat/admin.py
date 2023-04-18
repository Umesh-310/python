from django.contrib import admin

# Register your models here.
from .models import Category, Listing, Image, Message, Transaction, Review

admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Image)
admin.site.register(Message)
admin.site.register(Transaction)
admin.site.register(Review)


# class ListingAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'price', 'created_at')
#     list_filter = ('category', 'created_at')
#     search_fields = ('title', 'description')


# admin.site.register(Listing, ListingAdmin)
