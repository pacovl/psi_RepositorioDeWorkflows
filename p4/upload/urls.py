from django.conf.urls import url
from upload import views

urlpatterns = [
    url(r'^$', views.add_workflow, name='add_workflow')
]