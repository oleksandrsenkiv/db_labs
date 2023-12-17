from my_project.auth.dao import product_loading_dao
from my_project.auth.service.general_service import GeneralService


class ProductLoadingService(GeneralService):

    _dao = product_loading_dao

    def product_loading_find_technician(self, product_loading_id: int):
        return self._dao.product_loading_find_technician(product_loading_id)
