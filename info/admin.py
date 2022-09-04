from django.contrib import admin
from .models import Dept, Class, Assign, AssignTime, Course, Attendance, AttendanceClass, StudentCourse


# Register your models here.
@admin.register(Dept)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Class)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "dept", "sem", "section"]


@admin.register(Assign)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "class_id", "course", "teacher"]


@admin.register(AssignTime)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "assign", "period", "day"]


@admin.register(Course)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "dept", "name", "shortname"]


@admin.register(Attendance)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "course", "student","status", "date"]


@admin.register(AttendanceClass)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "assign", "date"]


@admin.register(StudentCourse)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id"]