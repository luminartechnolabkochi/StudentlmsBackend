from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from lms.models import Lead
from lms.serializers import LeadSerializer


class LeadListCreateView(ListAPIView,CreateAPIView):

    queryset=Lead.objects.all()

    serializer_class=LeadSerializer


class LeadRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    queryset=Lead.objects.all()

    serializer_class=LeadSerializer

