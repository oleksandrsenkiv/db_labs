
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import SnackAvailability
from my_project.auth.domain.orders.snack_availability import snacks_has_vm_menu
from my_project.auth.domain.orders.vm_menu import VmMenu
from my_project.auth.domain.orders.snacks import Snacks


class SnackAvailabilityDAO(GeneralDAO):

    _domain_type = SnackAvailability

    def snack_availability_find_vm_menu_snacks(self, snack_availability_id: int):
        """
        Find vm_menu and snacks associated with a specific snack_availability.
        :param snack_availability_id: ID of the snack_availability
        :return: List of VmMenu and Snacks objects associated with the snack_availability
        """
        session = self.get_session()

        associations = (
            session.query(snacks_has_vm_menu.c.vm_menu_id, snacks_has_vm_menu.c.snacks_id)
            .filter(snacks_has_vm_menu.c.snack_availability_id == snack_availability_id)
            .all()
        )

        vm_menu_ids, snacks_ids = zip(*associations)
        vm_menus = session.query(VmMenu).filter(VmMenu.id.in_(vm_menu_ids)).all()
        snacks = session.query(Snacks).filter(Snacks.id.in_(snacks_ids)).all()

        return {
            "vm_menus": [vm_menu.put_into_dto() for vm_menu in vm_menus],
            "snacks": [snack.put_into_dto() for snack in snacks]
        }
