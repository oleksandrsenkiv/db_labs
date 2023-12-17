
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Snacks
from my_project.auth.domain.orders.brand import snacks_has_brand
from my_project.auth.domain.orders.brand import Brand
from my_project.auth.domain.orders.snack_availability import snacks_has_vm_menu
from my_project.auth.domain.orders.snack_availability import SnackAvailability
from my_project.auth.domain.orders.vm_menu import VmMenu

class SnacksDAO(GeneralDAO):
    _domain_type = Snacks

    def snacks_find_brand(self, snacks_id: int):
        """
        Find solar system associated with a specific owner.
        :param snacks_id: ID of the owner
        :return: List of SolarSystem objects associated with the owner
        """
        session = self.get_session()

        brands_ids = (
            session.query(snacks_has_brand.c.brand_id)
            .filter(snacks_has_brand.c.snacks_id == snacks_id)
            .all()
        )
        brand_ids = [brand_id for (brand_id,) in brands_ids]
        brands = session.query(Brand).filter(Brand.id.in_(brand_ids)).all()
        return [brand.put_into_dto() for brand in brands]

    def snacks_find_snack_availability_vm_menu(self, snacks_id: int):
        """
        Find availability and vm_menu associated with a specific snack.
        :param snacks_id: ID of the snack
        :return: List of SnackAvailability and VmMenu objects associated with the snack
        """
        session = self.get_session()
        associations = (
            session.query(snacks_has_vm_menu.c.snack_availability_id, snacks_has_vm_menu.c.vm_menu_id)
            .filter(snacks_has_vm_menu.c.snacks_id == snacks_id)
            .all()
        )

        availability_ids, vm_menu_ids = zip(*associations)
        availabilities = session.query(SnackAvailability).filter(SnackAvailability.id.in_(availability_ids)).all()
        vm_menus = session.query(VmMenu).filter(VmMenu.id.in_(vm_menu_ids)).all()

        return {
            "availabilities": [availability.put_into_dto() for availability in availabilities],
            "vm_menus": [vm_menu.put_into_dto() for vm_menu in vm_menus]
        }