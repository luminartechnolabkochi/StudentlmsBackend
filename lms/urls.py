

from django.urls import path

from lms import views


urlpatterns=[
    path("leads/",views.LeadListCreateView.as_view()),
    path("leads/<int:pk>/",views.LeadRetrieveUpdateDestroyView.as_view()),
    


]