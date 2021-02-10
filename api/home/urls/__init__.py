from django.urls import re_path

from home.views.home import HomeSectionsView

urlpatterns = [
    re_path(r'^home/?$', HomeSectionsView.as_view(), name="home"),
]