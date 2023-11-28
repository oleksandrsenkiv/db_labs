
from my_project.auth.dao import brand_dao
from my_project.auth.service.general_service import GeneralService


class BrandService(GeneralService):

    _dao = brand_dao

    def brand_find_snacks(self, brand_id: int):
        return self._dao.brand_find_snacks(brand_id)
