
from my_project.auth.dao import brand_dao
from my_project.auth.service.general_service import GeneralService


class BrandService(GeneralService):

    _dao = brand_dao

    def brand_find_snacks(self, brand_id: int):
        return self._dao.brand_find_snacks(brand_id)

    def add_snacks_to_brand(self, brand_id: int, snacks_id: int):
        return self._dao.add_snacks_to_brand(brand_id, snacks_id)

    def remove_snack_from_brand(self, brand_id: int, snacks_id: int):
        return self._dao.remove_snack_from_brand(brand_id, snacks_id)

    def add_brand(self, insert_brand: str):
        return self._dao.add_brand(insert_brand)



