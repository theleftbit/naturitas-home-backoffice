from collections import OrderedDict

from rest_framework.fields import CharField, URLField
from rest_framework.serializers import ModelSerializer

from home.models import HomeSectionItem


class HomeSectionItemSerializer(ModelSerializer):
    id = CharField(source='naturitas_id', required=False, allow_blank=True)
    image = URLField(source='image_url')
    link = URLField(source='link_url')

    class Meta:
        model = HomeSectionItem
        fields = ('id', 'type', 'name', 'image', 'link', 'deeplink')

    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
