from django.core.management import BaseCommand

from home.utils.home_section import populate_home_sections
from home.utils.home_section_item import populate_home_section_items
from home.utils.home_section_item_type import populate_home_section_item_types
from home.utils.home_section_type import populate_home_section_types
from users.utils.user import create_superadmin_user


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_superadmin_user()
        populate_home_section_item_types()
        populate_home_section_types()
        populate_home_sections()
        populate_home_section_items()
