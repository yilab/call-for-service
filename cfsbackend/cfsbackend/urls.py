"""
    cfsbackend URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from cfsbackend.cfsapp import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'incidents', views.IncidentViewSet)
router.register(r'calls', views.CallViewSet)

# You must use the optional 3rd parameter here. or otherwise it changes the URL for calls.
# the same holds true for any double-usage of the same queryset model in the ViewSet. 
router.register(r'callsoverview', views.CallOverviewViewSet, 'callsoverview')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]


