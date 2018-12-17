from django.urls import path, re_path
from django.conf.urls import url
from firstaid_app import views





app_name = 'firstaid_app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('library_list/', views.LibraryListView.as_view(),name='library_list'),
    path('logout/', views.user_logout, name='logout'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    url(r'^library_list/(?P<pk>[-\w]+)/$', views.DiseaseDetailView.as_view(),name='detail'),
    url(r'^(?P<pk>[-\w]+)/$', views.DiseaseDetailView.as_view(),name='detail'),
    
]
