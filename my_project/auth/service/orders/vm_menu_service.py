
from my_project.auth.dao import vm_menu_dao
from my_project.auth.service.general_service import GeneralService


class VmMenuService(GeneralService):

    _dao = vm_menu_dao

    def vm_menu_find_snack_availability_snacks(self, vm_menu_id: int):
        return self._dao.vm_menu_find_snack_availability_snacks(vm_menu_id)
