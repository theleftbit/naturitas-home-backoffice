from django.db import models

class HomeSectionType(models.Model):
    HOME_SECTION_TYPE_BANNERS_ID = 1
    HOME_SECTION_TYPE_CATEGORIES_ID = 2
    HOME_SECTION_TYPE_BRANDS_ID = 3

    name = models.CharField(max_length=20, blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.name
