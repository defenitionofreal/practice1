from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class NonceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date',)

class JwtTokenAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date',)

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Сertificate)
admin.site.register(Nonce, NonceAdmin)
admin.site.register(JwtToken, JwtTokenAdmin)
