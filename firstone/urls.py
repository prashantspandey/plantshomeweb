from django.conf.urls import url, include
from . import views

app_name = 'firstone'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^all_plants/', views.AllPlantsView.as_view(), name='allPlants'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),

    url(r'^register/$', views.UserFormView.as_view(), name='registeruser'),
    url(r'^logout/$', views.user_logo, name='logout'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^search/', views.search, name='search'),
    url(r'^ordersubmit/$', views.ordersubmit, name='ordersubmit'),
    url(r'^ordered/$', views.confirmedorder, name='confirmorder'),
    url(r'^comingsoon/$', views.comingsoon, name='comingsoon'),
    url(r'^vendororder/$',views.vendororder,name='vendororder'),
    url(r'^previousvendororders/$',views.previousorders,name='previousorders'),
    url(r'^myorders/$',views.myorders,name='myorders'),
]
