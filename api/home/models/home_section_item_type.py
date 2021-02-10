from django.db import models

class HomeSectionItemType(models.Model):
    HOME_SECTION_ITEM_BANNERS_OFFERS_ID = 1
    HOME_SECTION_ITEM_BANNERS_BRAND_ID = 2
    HOME_SECTION_ITEM_BANNERS_CATEGORY_ID = 3

    name = models.CharField(max_length=20, blank=False, null=False)

    objects = models.Manager()
