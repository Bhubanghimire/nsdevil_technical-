from django.urls import path
from info import views

urlpatterns = [
    path('', views.index, name="index"),
    path('student/<slug:stud_id>/attendance/', views.attendance, name='attendance'),
    path('student/<slug:stud_id>/<slug:course_id>/attendance/', views.attendance_detail, name='attendance_detail'),
    path('student/<slug:stud_id>/marks_list/', views.marks_list, name='marks_list'),
    path('student/<slug:class_id>/timetable/', views.timetable, name='timetable'),
    path('teacher/<slug:teacher_id>/<int:choice>/Classes/', views.t_clas, name='t_clas'),
    path('teacher/<slug:teacher_id>/t_timetable/', views.t_timetable, name='t_timetable'),
    path('teacher/<int:asst_id>/Free_teachers/', views.free_teachers, name='free_teachers'),
    path('teacher/<int:assign_id>/ClassDates/', views.t_class_date, name='t_class_date'),
    path('teacher/<int:assign_id>/Extra_class/', views.t_extra_class, name='t_extra_class'),
    path('teacher/<int:assign_id>/Students/attendance/', views.t_student, name='t_student'),
    path('teacher/<int:assign_id>/Report/', views.t_report, name='t_report'),
    path('teacher/<slug:stud_id>/<slug:course_id>/attendance/', views.t_attendance_detail, name='t_attendance_detail'),
    path('teacher/<int:ass_c_id>/attendance/', views.t_attendance, name='t_attendance'),
    path('teacher/<int:ass_c_id>/Cancel/', views.cancel_class, name='cancel_class'),
    path('teacher/<int:ass_c_id>/attendance/confirm/', views.confirm, name='confirm'),
    path('teacher/<int:ass_c_id>/Edit_att/', views.edit_att, name='edit_att'),

]

