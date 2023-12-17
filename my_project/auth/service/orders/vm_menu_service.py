
from my_project.auth.dao import vm_menu_dao
from my_project.auth.service.general_service import GeneralService


class VmMenuService(GeneralService):

    _dao = vm_menu_dao

    def vm_menu_find_snack_availability_snacks(self, vm_menu_id: int):
        return self._dao.vm_menu_find_snack_availability_snacks(vm_menu_id)

    def add_snack_and_availability_to_vm_menu(self, vm_menu_id: int, snacks_id: int, snack_availability_id: int):
        return self._dao.add_snack_and_availability_to_vm_menu(vm_menu_id, snacks_id, snack_availability_id)

    def remove_snack_and_availability_from_vm_menu(self,  vm_menu_id: int, snacks_id: int, snack_availability_id: int):
        return self._dao.remove_snack_and_availability_from_vm_menu(vm_menu_id, snacks_id, snack_availability_id)
