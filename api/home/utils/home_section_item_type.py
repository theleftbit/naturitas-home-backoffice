import logging

from home.models import HomeSectionItemType


def populate_home_section_item_types():
    logging.getLogger('django').info('Populating home section item types')

    HomeSectionItemType.objects.update_or_create(id=HomeSectionItemType.HOME_SECTION_ITEM_BANNERS_OFFERS_ID,
                                                 defaults={
                                                     'id': HomeSectionItemType.HOME_SECTION_ITEM_BANNERS_OFFERS_ID,
                                                     'name': 'Offers'})
    HomeSectionItemType.objects.update_or_create(id=HomeSectionItemType.HOME_SECTION_ITEM_BANNERS_BRAND_ID,
                                                 defaults={
                                                     'id': HomeSectionItemType.HOME_SECTION_ITEM_BANNERS_BRAND_ID,
                                                     'name': 'Brand'})
    HomeSectionItemType.objects.update_or_create(id=HomeSectionItemType.HOME_SECTION_ITEM_BANNERS_CATEGORY_ID,
                                                 defaults={
                                                     'id': HomeSectionItemType.HOME_SECTION_ITEM_BANNERS_CATEGORY_ID,
                                                     'name': 'Category'})
