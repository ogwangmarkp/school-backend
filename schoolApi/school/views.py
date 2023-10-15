from rest_framework import viewsets
from .models import *
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from.serializers import SchoolSerializer

# Create your views here.
class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('-id')
    serializer_class = SchoolSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend, )
    filterset_fields = ['name', ]
    search_fields = ('name', )
    ordering_fields = ['name', ]
   
