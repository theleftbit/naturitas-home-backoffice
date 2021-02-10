import logging

from home.models.home_section_type import HomeSectionType
from home.models.home_section_item import HomeSectionItem

SECTIONS = [
    {
        'type_id': HomeSectionType.HOME_SECTION_BANNERS_ID,
        'items': [
            {
                "image": "banner_6euros_ES.jpg",
                "type": "offers",
                "link": "/ofertas"
            },
            {
                "image": "Header_home_naturitas_nuevo.jpg",
                "type": "brand",
                "id": "5482",
                "link": "/marca-propia-naturitas"
            },
            {
                "image": "Header_home_desk_natunew_ES.jpg",
                "type": "offers",
                "link": "/ofertas"
            },
            {
                "image": "Header_home_frescos_m2_ES.jpg",
                "type": "category",
                "id": "26092",
                "link": "/c/frescos"
            }
        ]
    },
    {
        'type_id': HomeSectionType.HOME_SECTION_CATEGORIES_ID,
        'items': [
            {
                "id": "26095",
                "name": "Suplementos",
                "image": "suplementos.jpg",
                "link": "/c/suplementos"
            },
            {
                "id": "26086",
                "name": "Alimentación",
                "image": "alimentacion.jpg",
                "link": "/c/alimentacion"
            },
            {
                "id": "26092",
                "name": "Frescos",
                "image": "frescos.jpg",
                "link": "/c/frescos"
            },
            {
                "id": "26080",
                "name": "Cosmética",
                "image": "cosmetica-e-higiene.jpg",
                "link": "/c/cosmetica-e-higiene"
            },
            {
                "id": "26089",
                "name": "Mamá y bebé",
                "image": "mama.jpg",
                "link": "/c/mama-y-bebe"
            },
            {
                "id": "26077",
                "name": "Hogar y huerto",
                "image": "hogar.jpg",
                "link": "/c/hogar-y-huerto"
            }
        ]
    },
    {
        'type_id': HomeSectionType.HOME_SECTION_BRANDS_ID,
        'items': [
            {
                "id": "7435",
                "name": "Bonusan",
                "image": "bonusan.jpg",
                "link": "/b/bonusan"
            },
            {
                "id": "7504",
                "name": "El Granero Integral",
                "image": "granero_integral.jpg",
                "link": "/b/el-granero-integral",
            },
            {
                "id": "4507",
                "name": "Lamberts",
                "image": "lamberts.jpg",
                "link": "/b/lamberts",
            },
            {
                "id": "5683",
                "name": "Nutergia",
                "image": "nutergia.jpg",
                "link": "/b/nutergia",
            },
            {
                "id": "4513",
                "name": "Solgar",
                "image": "solgar.jpg",
                "link": "/b/solgar",
            },
            {
                "id": "5482",
                "name": "Naturitas",
                "image": "naturitas.jpg",
                "link": "/marca-propia-naturitas",
            },
            {
                "id": "4705",
                "name": "Weleda",
                "image": "weleda.jpg",
                "link": "/b/weleda",
            },
            {
                "id": "5809",
                "name": "La Finestra sul Cielo",
                "image": "finestra.jpg",
                "link": "/b/la-finestra-sul-cielo",
            }
        ]
    }
]


def populate_home_section_items():
    logging.getLogger('django').info('Populating home section items')

    for section in SECTIONS:
        for item in section['items']:
            HomeSectionItem.objects.update_or_create(image_file_name=item['image'],
                                                     defaults={'section_id': section['type_id'],
                                                               'naturitas_id': item.get('id', None),
                                                               'name': item.get('name', None),
                                                               'image_file_name': item['image'],
                                                               'link_path': item['link'],
                                                               'type': item.get('type', None)})
