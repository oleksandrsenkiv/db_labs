
from my_project.auth.dao import snack_availability_dao
from my_project.auth.service.general_service import GeneralService


class SnackAvailabilityService(GeneralService):

    _dao = snack_availability_dao

    def snack_availability_find_vm_menu_snacks(self, snack_availability_id: int):
        return self._dao.snack_availability_find_vm_menu_snacks(snack_availability_id)

    def add_vm_menu_and_snack_to_availability(self, snack_availability_id: int, vm_menu_id: int, snacks_id: int):
        return self._dao.add_vm_menu_and_snack_to_availability(snack_availability_id, vm_menu_id, snacks_id)

    def remove_vm_menu_and_snack_from_availability(self, snack_availability_id: int, vm_menu_id: int, snacks_id: int):
        return self._dao.remove_vm_menu_and_snack_from_availability(snack_availability_id, vm_menu_id, snacks_id)
