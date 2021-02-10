from django.conf import settings
from django.db import models


class HomeSectionItem(models.Model):
    section = models.ForeignKey('HomeSection', blank=False, null=False, on_delete=models.CASCADE, related_name='items')
    naturitas_id = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=False, null=True)
    name = models.CharField(max_length=50, blank=False, null=True)
    image_file_name = models.CharField(max_length=100, blank=False, null=False)
    link_path = models.URLField(max_length=200, blank=False, null=False)

    objects = models.Manager()

    @property
    def image_url(self):
        return f'{settings.PUBLIC_WEB_BASE_URL}{self.section.images_path}{self.link_path}'

    @property
    def link_url(self):
        return f'{settings.PUBLIC_WEB_BASE_URL}{self.link_path}'

    @property
    def deeplink(self):
        return f'{settings.PUBLIC_WEB_BASE_URL}{self.section.deeplink_path}/{self.naturitas_id}'
