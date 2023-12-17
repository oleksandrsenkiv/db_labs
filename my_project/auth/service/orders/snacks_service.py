
from my_project.auth.dao import snacks_dao
from my_project.auth.service.general_service import GeneralService


class SnacksService(GeneralService):

    _dao = snacks_dao

    def snacks_find_brand(self, snacks_id: int):
        return self._dao.snacks_find_brand(snacks_id)

    def snacks_find_snack_availability_vm_menu(self, snacks_id: int):
        return self._dao.snacks_find_snack_availability_vm_menu(snacks_id)
