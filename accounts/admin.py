from django.contrib import admin
from accounts.models import User, Teacher, Student
from django.db import models
from django.utils.html import mark_safe
from django.contrib.admin.widgets import AdminFileWidget

# Register your models here.
class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f' <a href="{image_url}" target="_blank">'
                f'  <img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))

@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["id",'email', 'full_name', 'phone']
    fieldsets = (
        ('General Info', {
            'fields': ('full_name', 'profile', 'email', "gender", "phone")
        }),
        ('Permission', {
            'fields': ('is_admin', 'is_staff', "is_active","added_by_admin")
        }),
    )
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }
    readonly_fields = ["email", ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["user"]