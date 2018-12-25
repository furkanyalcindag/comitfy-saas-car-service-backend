from django.conf.urls import url
from django.urls import path
from .import views


app_name = 'patient'

urlpatterns = [
    # path('patients/', ListPatientView.as_view(), name="patients-all"),
    url(r'^$', views.patients_list, name='index'),

    url(r'json/$', views.patients_listJson, name='jsonPatient'),

url(r'^getPatient/(?P<pk>\d+)$', views.getPatient, name='getPatient'),

    url(r'^hasta/ekle/$', views.patients_add, name='hasta-ekle'),

    url(r'^hasta/ekles/$', views.patiends_add2, name='hasta-ekle2'),

    url(r'^hasta/duzenle/(?P<pk>\d+)$', views.patient_update, name='hasta-duzenle'),

    url(r'^hasta/sil/(?P<pk>\d+)$', views.patient_delete, name='hasta-sil'),
]
