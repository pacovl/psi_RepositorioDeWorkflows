from django.conf.urls import url
from data import views 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_workflow/$', views.add_workflow, name='add_workflow'),
    url(r'^workflow/(?P<workflow_name_slug>[\w\-]+)/$', views.show_workflow, name='show_workflow'),
]
