from rest_framework.serializers import ModelSerializer

from home.models.home_section import HomeSection
from home.serializers.home_item import HomeSectionItemSerializer


class HomeSectionSerializer(ModelSerializer):
    items = HomeSectionItemSerializer(many=True)

    class Meta:
        model = HomeSection
        fields = ('type', 'priority', 'items')
