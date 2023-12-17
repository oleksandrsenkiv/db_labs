
from my_project.auth.dao import snack_availability_dao
from my_project.auth.service.general_service import GeneralService


class SnackAvailabilityService(GeneralService):

    _dao = snack_availability_dao

    def snack_availability_find_vm_menu_snacks(self, snack_availability_id: int):
        return self._dao.snack_availability_find_vm_menu_snacks(snack_availability_id)
