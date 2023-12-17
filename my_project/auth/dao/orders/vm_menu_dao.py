from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import VmMenu
from my_project.auth.domain.orders.snack_availability import SnackAvailability
from my_project.auth.domain.orders.snack_availability import snacks_has_vm_menu
from my_project.auth.domain.orders.snacks import Snacks



class VmMenuDAO(GeneralDAO):
    _domain_type = VmMenu

    def vm_menu_find_snack_availability_snacks(self, vm_menu_id: int):
        """
        Find snack_availability_id and snacks associated with a specific vm_menu.
        :param vm_menu_id: ID of the vm_menu
        :return: List of SnackAvailability and Snacks objects associated with the vm_menu
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the snack_availability_id and snacks IDs associated with the vm_menu
        associations = (
            session.query(snacks_has_vm_menu.c.snack_availability_id, snacks_has_vm_menu.c.snacks_id)
            .filter(snacks_has_vm_menu.c.vm_menu_id == vm_menu_id)
            .all()
        )

        # Extract snack_availability_id and snacks IDs from the result
        snack_availability_ids, snacks_ids = zip(*associations)

        # Query the SnackAvailability and Snacks tables to get the objects associated with the IDs
        snack_availabilities = session.query(SnackAvailability).filter(
            SnackAvailability.id.in_(snack_availability_ids)).all()
        snacks = session.query(Snacks).filter(Snacks.id.in_(snacks_ids)).all()

        return {
            "snack_availabilities": [availability.put_into_dto() for availability in snack_availabilities],
            "snacks": [snack.put_into_dto() for snack in snacks]
        }

