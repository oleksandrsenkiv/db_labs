
from my_project.auth.service import vm_menu_service
from my_project.auth.controller.general_controller import GeneralController


class VmMenuController(GeneralController):

    _service = vm_menu_service

    def vm_menu_find_snack_availability_snacks(self, vm_menu_id: int):
        return self._service.vm_menu_find_snack_availability_snacks(vm_menu_id)

    def add_snack_and_availability_to_vm_menu(self, vm_menu_id: int, snacks_id: int, snack_availability_id: int):
        return self._service.add_snack_and_availability_to_vm_menu(vm_menu_id, snacks_id, snack_availability_id)

    def remove_snack_and_availability_from_vm_menu(self, vm_menu_id: int, snacks_id: int, snack_availability_id: int):
        return self._service.remove_snack_and_availability_from_vm_menu(vm_menu_id, snacks_id, snack_availability_id)
