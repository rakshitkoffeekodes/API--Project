from django.urls import path
from app_crud import views

urlpatterns = [
    path('', views.home, name='home'),
    path('School/<str:sn>/<str:sa>/<str:snum>/<str:se>', views.School),
    path('all_School', views.all_School),
    path('del_School/<int:pk>', views.del_School),
    path('up_School/<int:pk>/<str:sn>/<str:sa>/<str:snum>/<str:se>', views.up_School),
    path('add_student/<str:sn>/<str:ssn>/<str:ss>/<str:sa>/<str:aa>/<str:sc>/<sf>', views.add_student),
    path('all_student', views.all_student),
    path('del_student/<int:pk>', views.del_student),
    path('up_student/<int:pk>/<str:sn>/<str:ssn>/<str:ss>/<str:sa>/<str:aa>/<str:sc>/<sf>', views.up_student),
    path('add_teacher/<str:tn>/<str:stn>/<str:ct>/<str:ts>', views.add_teacher),
    path('all_teacher', views.all_teacher),
    path('del_teacher/<int:pk>', views.del_teacher),
    path('up_teacher/<int:pk>/<str:tn>/<str:stn>/<str:ct>/<str:ts>', views.up_teacher),
    path('add_clark/<str:cn>/<str:cp>/<str:cs>', views.add_clark),
    path('all_clark', views.all_clark),
    path('del_clark/<int:pk>', views.del_clark),
    path('up_clark/<int:pk>/<str:cn>/<str:cp>/<str:cs>', views.up_clark),
    path('add_course/<str:c>/<str:f>', views.add_course),
    path('all_course', views.all_course),
    path('del_course/<int:pk>', views.del_course),
    path('up_course/<int:pk>/<str:c>/<str:f>', views.up_course),
    path('view_course/<str:c>', views.view_course),
    path('add_bus/<str:dn>/<str:br>/<str:sb>', views.add_bus),
    path('all_bus', views.all_bus),
    path('del_bus/<int:pk>', views.del_bus),
    path('up_bus/<int:pk>/<str:dn>/<str:br>/<str:sb>', views.up_bus),
    path('view_area/<str:aa>', views.view_area),
    # path('add_salary/<str:ts>/<str:tn>',views.add_salary),
    path('all_staf_salary',views.all_staf_salary)
]
