
from my_project.auth.service import vm_menu_service
from my_project.auth.controller.general_controller import GeneralController


class VmMenuController(GeneralController):

    _service = vm_menu_service

    def vm_menu_find_snack_availability_snacks(self, vm_menu_id: int):
        return self._service.vm_menu_find_snack_availability_snacks(vm_menu_id)
