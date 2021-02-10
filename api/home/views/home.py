from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from home.models import HomeSection
from home.serializers.home_section import HomeSectionSerializer


class HomeSectionsView(ListAPIView):
    serializer_class = HomeSectionSerializer
    permission_classes = (AllowAny,)
    queryset =  HomeSection.objects.all()
