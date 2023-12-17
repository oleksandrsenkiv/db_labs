
from my_project.auth.service import brand_service
from my_project.auth.controller.general_controller import GeneralController


class BrandController(GeneralController):

    _service = brand_service
    def brand_find_snacks(self, brand_id: int):
        return self._service.brand_find_snacks(brand_id)
