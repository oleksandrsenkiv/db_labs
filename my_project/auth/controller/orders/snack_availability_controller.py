
from my_project.auth.service import snack_availability_service
from my_project.auth.controller.general_controller import GeneralController


class SnackAvailabilityController(GeneralController):

    _service = snack_availability_service

    def snack_availability_find_vm_menu_snacks(self, snack_availability_id: int):
        return self._service.snack_availability_find_vm_menu_snacks(snack_availability_id)