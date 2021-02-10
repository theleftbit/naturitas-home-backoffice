import logging

from home.models import HomeSectionType
from home.models.home_section import HomeSection


def populate_home_sections():
    logging.getLogger('django').info('Populating home sections')

    HomeSection.objects.update_or_create(type_id=HomeSectionType.HOME_SECTION_BANNERS_ID,
                                         defaults={'type_id': HomeSectionType.HOME_SECTION_BANNERS_ID,
                                                   'priority': 100,
                                                   'images_path': '/media/interactiv4/slidermanager/banner',
                                                   'deeplink_path': ''})

    HomeSection.objects.update_or_create(type_id=HomeSectionType.HOME_SECTION_CATEGORIES_ID,
                                         defaults={'type_id': HomeSectionType.HOME_SECTION_CATEGORIES_ID,
                                                   'priority': 20,
                                                   'title': 'Categorías',
                                                   'images_path': '/media/wysiwyg/common',
                                                   'deeplink_path': '/c'})

    HomeSection.objects.update_or_create(type_id=HomeSectionType.HOME_SECTION_BRANDS_ID,
                                         defaults={'type_id': HomeSectionType.HOME_SECTION_BRANDS_ID,
                                                   'priority': 10,
                                                   'title': 'Las marcas más populares',
                                                   'images_path': '/media/wysiwyg/es/featured-brands',
                                                   'deeplink_path': '/b'})
