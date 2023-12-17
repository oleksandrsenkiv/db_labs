
from my_project.auth.service import brand_service
from my_project.auth.controller.general_controller import GeneralController


class BrandController(GeneralController):

    _service = brand_service

    def brand_find_snacks(self, brand_id: int):
        return self._service.brand_find_snacks(brand_id)

    def add_snacks_to_brand(self, brand_id: int, snacks_id: int):
        return self._service.add_snacks_to_brand(brand_id, snacks_id)

    def remove_snack_from_brand(self, brand_id: int, snacks_id: int):
        return self._service.remove_snack_from_brand(brand_id, snacks_id)

    def add_brand(self, insert_brand: str):
        return self._service.add_brand(insert_brand)


