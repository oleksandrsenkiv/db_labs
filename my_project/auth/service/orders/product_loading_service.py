from my_project.auth.dao import product_loading_dao
from my_project.auth.service.general_service import GeneralService


class ProductLoadingService(GeneralService):

    _dao = product_loading_dao

    def product_loading_find_technician(self, product_loading_id: int):
        return self._dao.product_loading_find_technician(product_loading_id)

    def get_product_loading_stats(self, stats_type: str):
        return self._dao.get_product_loading_stats(stats_type)
