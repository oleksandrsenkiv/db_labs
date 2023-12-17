from my_project.auth.service import product_loading_service
from my_project.auth.controller.general_controller import GeneralController


class ProductLoadingController(GeneralController):

    _service = product_loading_service

    def product_loading_find_technician(self, product_loading_id: int):
        return self._service.product_loading_find_technician(product_loading_id)

    def get_product_loading_stats(self, stats_type: str):
        return self._service.get_product_loading_stats(stats_type)
