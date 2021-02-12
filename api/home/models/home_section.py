from django.db import models


class HomeSection(models.Model):
    HOME_SECTION_BANNERS_ID = 1
    HOME_SECTION_CATEGORIES_ID = 2
    HOME_SECTION_BRANDS_ID = 3

    type = models.ForeignKey('HomeSectionType', blank=False, null=False, on_delete=models.CASCADE,
                             related_name='sections')
    title = models.CharField(max_length=50, blank=True, null=True)
    priority = models.IntegerField(null=False)
    images_path = models.CharField(max_length=200, blank=False, null=False)
    deeplink_path = models.CharField(max_length=3, blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.type.__str__()
