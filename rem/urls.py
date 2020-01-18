from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'rem'

urlpatterns = [
    path('new/',views.CreateRem.as_view(),name = "createrem"),
    path('remlist/',views.ListRem.as_view(),name = "remlist"),
    url(r'^rem/(?P<pk>\d+)/edit/$',views.UpdateRem.as_view(),name = "updaterem"),
]
