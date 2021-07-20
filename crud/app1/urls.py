from django.urls import path, include
from app1 import views
urlpatterns = [
    path('',views.add_show,name='addandshow'),
    path('<int:id>/',views.delete_data, name='deletedata'),
    path('update/<int:id>/',views.update_data, name='updatedata')

]