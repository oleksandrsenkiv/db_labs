
from my_project.auth.service import snacks_service
from my_project.auth.controller.general_controller import GeneralController


class SnacksController(GeneralController):

    _service = snacks_service

    def snacks_find_brand(self, snacks_id: int):
        return self._service.snacks_find_brand(snacks_id)

    def snacks_find_snack_availability_vm_menu(self, snacks_id: int):
        return self._service.snacks_find_snack_availability_vm_menu(snacks_id)

    def add_brand_to_snack(self, brand_id: int, snacks_id: int):
        return self._service.add_brand_to_snack(brand_id, snacks_id)

    def remove_brand_from_snack(self, snacks_id: int, brand_id: int,):
        return self._service.remove_brand_from_snack(snacks_id, brand_id)

    def add_vm_menu_and_availability_to_snack(self, snacks_id: int, vm_menu_id: int, snack_availability_id: int):
        return self._service.add_vm_menu_and_availability_to_snack(snacks_id, vm_menu_id, snack_availability_id)

    def remove_vm_menu_and_availability_from_snack(self,  snacks_id: int, vm_menu_id: int, snack_availability_id: int):
        return self._service.remove_vm_menu_and_availability_from_snack(snacks_id, vm_menu_id, snack_availability_id )

    def insert_ten_no_name_snacks(self):
        return self._service.insert_ten_no_name_snacks()

    def insert_in_snacks_has_brand(self, insert_brand_name: str, insert_snack_name: str):
        return self._service.insert_in_snacks_has_brand(insert_brand_name, insert_snack_name)

    def create_db_from_snacks(self):
        return self._service.create_db_from_snacks()