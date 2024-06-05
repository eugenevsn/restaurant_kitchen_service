from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import DishType, Cook, Dish


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Cook)
class CookAdminAdmin(UserAdmin):
    ordering = ("first_name", )
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('years_of_experience',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': (
            "first_name",
            'last_name',
            'email',
            'years_of_experience',
        )}),
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass
