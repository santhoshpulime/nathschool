from django.urls import path
from . import views
urlpatterns = [
    

    path('',views.class_room,name='class_room'),
    path('signup/',views.signup,name='signup'),
    path('show_students/<int:pk>',views.show_students,name='show_students'),
    path('class_for_school/',views.class_for_school,name='class_for_school'),
   
    path('login/',views.login,name='login'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('show_student_name_login',views.show_student_name_login,name='show_student_name_login'),
    path('logout/',views.logout,name='logout'),
    path('studentpage/<int:pk>',views.studentpage,name='studentpage'),
    path('fill_stu',views.fill_stu,name='fill_stu'),
    path('show_students_data_mouse_click',views.show_students_data_mouse_click,name='show_students_data_mouse_click'),
    path('get_stu_data_to_marks',views.get_stu_data_to_marks,name='get_stu_data_to_marks'),
    path('save_student_marks',views.save_student_marks,name='save_student_marks'),
    path('show_student_marks_for_school',views.show_student_marks_for_school,name='show_student_marks_for_school'),
    path('editmarks',views.editmarks,name='editmarks'),
    path('deletemarks',views.deletemarks,name='deletemarks'),
    path('some/',views.some,name='some'),
    path('deletestudent',views.deletestudent,name='deletestudent'),
    path('editstudent',views.editstudent,name='editstudent'),
    path('search',views.search,name='search'),


]