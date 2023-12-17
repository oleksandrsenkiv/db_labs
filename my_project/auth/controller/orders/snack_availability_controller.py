
from my_project.auth.service import snack_availability_service
from my_project.auth.controller.general_controller import GeneralController


class SnackAvailabilityController(GeneralController):

    _service = snack_availability_service

    def snack_availability_find_vm_menu_snacks(self, snack_availability_id: int):
        return self._service.snack_availability_find_vm_menu_snacks(snack_availability_id)

    def add_vm_menu_and_snack_to_availability(self, snack_availability_id: int, vm_menu_id: int, snacks_id: int):
        return self._service.add_vm_menu_and_snack_to_availability(snack_availability_id, vm_menu_id, snacks_id)

    def remove_vm_menu_and_snack_from_availability(self, snack_availability_id: int, vm_menu_id: int, snacks_id: int):
        return self._service.remove_vm_menu_and_snack_from_availability(snack_availability_id, vm_menu_id, snacks_id)