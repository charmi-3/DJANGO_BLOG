from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(),name='home_page'),
    path('addblog',CreateBlog,name='addblog_page'),
    path('detail/<int:pk>',Detail.as_view(),name='detail_page'),
    path('delete/<int:pk>',Delete.as_view(),name='delete_page'),
    path('edit/<int:pk>',Edit.as_view(),name='edit_page'),
]