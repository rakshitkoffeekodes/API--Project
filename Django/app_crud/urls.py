from django.urls import path
from app_crud import views

urlpatterns = [
    path('', views.home, name='home'),
    path('School/<str:n>/<str:a>/<str:c>/<str:s>/<str:co>', views.School),
    path('all_School', views.all_School),
    path('del_School/<int:pk>', views.del_School),
    path('up_School/<int:pk>/<str:n>/<str:a>/<str:c>/<str:s>/<str:co>', views.up_School),
    path('add_student/<str:sn>/<str:ssn>/<str:ss>',views.add_student),
    path('all_student',views.all_student),
    path('del_student/<int:pk>',views.del_student),
    path('up_student/<int:pk>/<str:sn>/<str:ssn>/<str:ss>',views.up_student),
    path('add_teacher/<str:tn>/<str:stn>/<str:ct>',views.add_teacher),
    path('all_teacher',views.all_teacher),
    path('del_teacher/<int:pk>',views.del_teacher),
    path('up_teacher/<int:pk>/<str:tn>/<str:stn>/<str:ct>',views.up_teacher),
    path('add_clark/<str:cn>/<str:cp>/<str:cs>',views.add_clark),
    path('all_clark',views.all_clark),
    path('del_clark/<int:pk>',views.del_clark),
    path('up_clark/<int:pk>/<str:cn>/<str:cp>/<str:cs>',views.up_clark)
]
