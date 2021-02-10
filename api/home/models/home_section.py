from django.db import models


class HomeSection(models.Model):
    type = models.ForeignKey('HomeSectionType', blank=False, null=False, on_delete=models.CASCADE,
                             related_name='sections')
    title = models.CharField(max_length=50, blank=True, null=True)
    priority = models.IntegerField(null=False)
    images_path = models.CharField(max_length=200, blank=False, null=False)
    deeplink_path = models.CharField(max_length=3, blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.type.__str__()
