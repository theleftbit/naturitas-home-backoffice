import logging

from home.models.home_section_type import HomeSectionType


def populate_home_section_types():
    logging.getLogger('django').info('Populating home section types')

    HomeSectionType.objects.update_or_create(id=HomeSectionType.HOME_SECTION_TYPE_BANNERS_ID,
                                             defaults={'id': HomeSectionType.HOME_SECTION_TYPE_BANNERS_ID,
                                                       'name': 'Banners'})
    HomeSectionType.objects.update_or_create(id=HomeSectionType.HOME_SECTION_TYPE_CATEGORIES_ID,
                                             defaults={'id': HomeSectionType.HOME_SECTION_TYPE_CATEGORIES_ID,
                                                       'name': 'Categories'})
    HomeSectionType.objects.update_or_create(id=HomeSectionType.HOME_SECTION_TYPE_BRANDS_ID,
                                             defaults={'id': HomeSectionType.HOME_SECTION_TYPE_BRANDS_ID,
                                                       'name': 'Brands'})
