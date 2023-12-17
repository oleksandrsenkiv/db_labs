
from my_project.auth.service import snacks_service
from my_project.auth.controller.general_controller import GeneralController


class SnacksController(GeneralController):

    _service = snacks_service

    def snacks_find_brand(self, snacks_id: int):
        return self._service.snacks_find_brand(snacks_id)

    def snacks_find_snack_availability_vm_menu(self, snacks_id: int):
        return self._service.snacks_find_snack_availability_vm_menu(snacks_id)
